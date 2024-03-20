<template>
    <Tree :nodes="nodes" :config="config" @nodeFocus="focusNode"></Tree>
</template>

<script setup>
/* Import any necessary modules or components */
import { ref } from 'vue';
import Tree from 'vue3-treeview';
import "vue3-treeview/dist/style.css";

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
const focusNode = (node) => {
    console.log(node.id);
}
const openNode = (node, closeElse = true) => {
    if (closeElse) closeAll;
    const parents = getNodeParents(node);
    parents.reverse();

    parents.forEach(node => { node.state.opened = true; });
    node.state.opened = true;
};

const openNodeByDepth = (depth) => {
    const nodes = getNodesByDepth(depth);
    console.log(nodes);
    nodes.forEach(node => { openNode(node, false); });
}

// initailize config
config.value.roots = [];
nodes_for_search.value.forEach(node => {
    const node_in_tree = getNodeByID(node.id);
    if (getNodeParent(node_in_tree) === null) config.value.roots.push(node_in_tree.id);
})

</script>


<style scoped>
/* Your scoped styles go here */
</style>