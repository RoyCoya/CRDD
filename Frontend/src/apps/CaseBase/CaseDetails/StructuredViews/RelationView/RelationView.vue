<template>
    <v-container>
        <div v-if="1" ref="relation_network" class="border rounded w-auto" style="height: 75vh;"></div>
    </v-container>
</template>

<script setup>
/* Import */
import { onMounted, ref } from 'vue';
import { Network, DataSet } from 'vis-network/dist/vis-network';

/* Data */
const nodes = ref(new DataSet([
    {
        "id": "1", "label": "基本信息", "color": "green", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "2", "label": "性别：男性", "color": "blue", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "3", "label": "民族：藏族", "color": "blue", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "4", "label": "年龄：76", "color": "blue", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "5", "label": "年龄单位：年", "color": "blue", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "6", "label": "既往史", "color": "green", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "7", "label": "症状：便血", "color": "red", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "8", "label": "时间点：入院前16年", "color": "orange", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "9", "label": "症状：瘀斑", "color": "red", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "10", "label": "时间点：入院前8年", "color": "orange", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "11", "label": "趋势：加重", "color": "purple", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "12", "label": "时间点：入院前1年", "color": "orange", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "13", "label": "症状：便血", "color": "red", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "14", "label": "趋势：加重", "color": "purple", "shape": "box", font: {
            color: "white"
        }
    },
    {
        "id": "15", "label": "时间点：入院前1年", "color": "orange", "shape": "box", font: {
            color: "white"
        }
    }
]))

const edges = ref(new DataSet([
    {
        "from": "1",
        "to": "2",
        "label": "包括",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "1",
        "to": "3",
        "label": "包括",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "1",
        "to": "4",
        "label": "包括",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "4",
        "to": "5",
        "label": "单位",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "6",
        "to": "7",
        "label": "描述症状",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "7",
        "to": "8",
        "label": "发生于",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "6",
        "to": "9",
        "label": "描述症状",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "9",
        "to": "10",
        "label": "发生于",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "9",
        "to": "11",
        "label": "趋势",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "11",
        "to": "12",
        "label": "发生于",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "6",
        "to": "13",
        "label": "描述症状",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "13",
        "to": "14",
        "label": "趋势",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    },
    {
        "from": "14",
        "to": "15",
        "label": "发生于",
        "arrows": "to",
        "scaling": {
            "label": true
        }
    }
]))

var graph_data = {
    nodes: nodes.value,
    edges: edges.value,
};

var options = {
    autoResize: true,
    height: '100%',
    width: '100%',
    physics: {
        enabled: true,
        solver: 'repulsion', // 或者选择其他适合的求解器
        repulsion: {
            centralGravity: 0.1,
            springLength: 130, // 调整弹簧长度，使节点间距更大
            springConstant: 0.05,
            nodeDistance: 130 // 调整节点之间的最小距离
        }
    }
};

const relation_network = ref(null);


/* Functions */

const fetchData = (network) => {
    // retrieve data

}

/* Define things you need to do on mounted */
onMounted(async () => {
    const container = relation_network.value;
    var network = new Network(container, graph_data, options);
    network.selectNodes(["error"])
    fetchData(network);
});
</script>

<style scoped>
/* Your scoped styles go here */
</style>