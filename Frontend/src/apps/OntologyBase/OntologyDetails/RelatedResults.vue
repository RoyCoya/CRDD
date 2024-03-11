<template>
  <!-- <v-btn @click="testFunc">test</v-btn> -->
  <div ref="relation_network" class="border rounded mt-3"></div>
</template>

<script setup>
// Import any necessary modules or components
import { onMounted, ref } from 'vue';
import { Network, DataSet } from 'vis-network/dist/vis-network';

// Define your component's data using ref
const nodes = new DataSet([
  { id: 1, label: '本体 1', shape:'circle' },
  { id: 2, label: '本体 2' , color:'pink', shape:'circle'},
  { id: 3, label: '本体 3', shape:'circle'  },
  { id: 4, label: '本体 4', shape:'circle'  },
  { id: 5, label: '本体 5', shape:'circle'  },
]);

// create an array with edges
const edges = new DataSet([
  { from: 2, to: 3, label:'属于'},
  { from: 2, to: 1 , label:'属于'},
  { from: 2, to: 4 , label:'同义'},
  { from: 2, to: 5 , label:'对立' }
]);

var data = {
  nodes: nodes,
  edges: edges
};

var options = {
  autoResize: true,
  height: '600px',
  width: '100%'
};
const relation_network = ref(null);

onMounted(() =>{
  const container = relation_network.value;
  // initialize network
  var network = new Network(container, data, options);
  network.selectNodes([2])
});

// const testFunc = () => {
//   data.edges = null
//   const container = relation_network.value;
//   var network = new Network(container, data, options);
// };

</script>

<script>

</script>

<style scoped>
/* Your scoped styles go here */
</style>