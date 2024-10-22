<!-- TODO -->

<template>
  <!-- <v-btn @click="testFunc">test</v-btn> -->
  <div v-if="1" ref="relation_network" class="border rounded mt-3 w-auto" style="height: 75vh;"></div>
  <div v-else><v-progress-circular :size="20" indeterminate color="primary"></v-progress-circular></div>
</template>

<script setup>
/* Import */
import { onMounted, ref } from 'vue';
import { getRelations, getPreferTermList, retrieve } from '@/apps/OntologyBase/ConceptDetails/concept';
import { Network, DataSet } from 'vis-network/dist/vis-network';

/* Data */
const props = defineProps({
  concept: {
    type: Object,
    required: true
  },
});

// initial data
const data = ref(null)

const nodes = ref(new DataSet([
  { id: "error", label: '暂无数据或获取异常', color: 'pink', shape: 'box' },
]))

const edges = ref(new DataSet([]))

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

const fetchData = async (network) => {
  // retrieve data
  let response = await getRelations(props.concept)
  let relations = response.data
  if (relations.length > 0) { nodes.value.remove(["error"]) }

  // get concepts with 1 representation
  let node_set = new Set()
  relations.forEach(relation => {
    node_set.add(relation.start)
    node_set.add(relation.end)
  });
  let concept_ids = Array.from(node_set)
  for (const id of concept_ids) {
    let node = await assembleNode(id);
    nodes.value.add([node]);
    
  }
  relations.forEach(relation => {
    let edge = {
      from: relation.start,
      to: relation.end,
      label: relation.relation,
      arrows:"to",
      scaling:{
      label: true,
    },
    }
    edges.value.add([edge])
  })
}

const assembleNode = async (id) => {
  let response = await retrieve(id)
  let concept_temp = response.data[0]
  let label = await getRepresentation(concept_temp)
  let node = {
    id: id,
    label: label,
    color: id == props.concept.element_id ? "red" : "green",
    shape: 'box',
    font:{
      color:"white"
    }
  }
  return node
}

const getRepresentation = async (concept) => {
  let result = await getPreferTermList(concept, { limit: 1 })
  if (result.length < 1) return "?"
  return result[0]
}

/* Define things you need to do on mounted */

onMounted(async () => {
  const container = relation_network.value;
  var network = new Network(container, graph_data, options);
  network.selectNodes(["error"])
  fetchData(network);
});

</script>

<script>

</script>

<style scoped>
/* Your scoped styles go here */
</style>