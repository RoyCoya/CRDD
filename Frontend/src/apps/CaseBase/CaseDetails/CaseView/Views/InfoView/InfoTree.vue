<template>
    <Tree :nodes="nodes" :config="config" @nodeFocus="focusNode" @nodeBlur="blurNode"></Tree>
</template>

<script setup>
/* Import any necessary modules or components */
import { ref, onMounted } from 'vue';
import Tree from 'vue3-treeview';
import "@/assets/css/treeview.css";
import { emitter } from '@/apps/CaseBase/CaseDetails/CaseView/emitter';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const props = defineProps({
    nodes_obj: Object,
    nodes_array: Array,
    config: Object,
});
const config = ref(props.config);
const nodes = ref(props.nodes_obj);
const nodes_for_search = ref(props.nodes_array);

/* Define your functions */

// node utilities
const getNodeByID = (id) => { return nodes.value[id]; }

const getNodeParent = (node) => {
    const parent = nodes_for_search.value.find(parent => parent.children.includes(node.id));
    if (parent) return getNodeByID(parent.id);
    else return null;
}

const getNodeBrothers = (node) => {
    const parent = getNodeParent(node);
    const brothers = [];
    var children = undefined;
    if (parent) {
        children = parent.children.slice();
    }
    else {
        children = config.value.roots.slice();
    }
    const current_node_index = children.findIndex(id => id === node.id);
    children.splice(current_node_index, 1);
    children.forEach(brother_id => {
        brothers.push(getNodeByID(brother_id));
    });
    return brothers;
}

const getNodeParents = (node) => {
    var parents = [];
    while (getNodeParent(node) != null) {
        parents.push(getNodeParent(node));
        node = getNodeParent(node);
    };
    return parents;
}

const getNodesByDepth = (depth) => {
    const results = nodes_for_search.value.filter(node => node.depth === depth);
    var nodes = [];
    results.forEach(node => { nodes.push(getNodeByID(node.id)) });
    return nodes;
};

const openAll = () => {
    nodes_for_search.value.forEach(node => {
        getNodeByID(node.id).state.opened = true;
    });
};

const closeAll = () => {
    nodes_for_search.value.forEach(node => {
        getNodeByID(node.id).state.opened = false;
    });
};

const openNode = (node, closeElse = true) => {
    if (closeElse) closeAll();
    const parents = getNodeParents(node);
    parents.reverse();

    parents.forEach(node => { node.state.opened = true; });
    node.state.opened = true;
};

const openNodeByDepth = (depth) => {
    closeAll();
    const nodes = getNodesByDepth(depth - 1);
    nodes.forEach(node => { openNode(node, false); });
}

const focusNode = (node, showBrothers = true) => {
    openNode(node);
    // open children deeper by one level
    // node.state.opened = !node.state.opened)

    // interaction with origin records
    var annotationsToShow = [];
    annotationsToShow.push(node);
    if (showBrothers) {
        const brothers = getNodeBrothers(node);
        brothers.forEach(brother => annotationsToShow.push(brother));
    }
    emitter.emit('focusNodeOnTreeview', annotationsToShow);
}

const blurNode = (node) => {
    emitter.emit('blurNodeOnTreeView');
}

// initailize config
config.value.roots = [];
nodes_for_search.value.forEach(node => {
    const node_in_tree = getNodeByID(node.id);
    if (getNodeParent(node_in_tree) === null) config.value.roots.push(node_in_tree.id);
})

// page setup
openNodeByDepth(0);

onMounted(() => {
    emitter.on('focusAnnotation', node_id => {
        // const node = getNodeByID(node_id)
        // focusNode(node);
        console.log(`annotation focused, should focus node ${node_id}`);
    });
});
// getNodeByID(1).focus()
</script>

<style scoped>
/* Your scoped styles go here */
</style>