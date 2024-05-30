<template>
  <!-- <v-btn @click="testFunc">test</v-btn> -->
  <div ref="relation_network" class="border rounded mt-3 bg-white"></div>
</template>

<script setup>
// Import any necessary modules or components
import { onMounted, ref } from 'vue';
import { Network, DataSet } from 'vis-network/dist/vis-network';

// Define your component's data using ref
// const nodes = new DataSet([
//   { id: 1, label: 'Concept 301', color:'pink', shape:'circle' },
//   { id: 2, label: '色盒子蛋白同源物8' , color:'yellow', shape:'box'},
//   { id: 3, label: 'chromobox protein homolog 8', color:'yellow', shape:'box'},
//   { id: 4, label: 'CBX8', color:'yellow', shape:'box'},
//   { id: 5, label: 'TM68984006', color:"green", shape:'diamond'},
//   { id: 6, label: 'BIOS Term ID', color:"grey", shape:'box'},
// ]);

// // create an array with edges
// const edges = new DataSet([
//   { from: 1, to: 2, label:'使用术语'},
//   { from: 1, to: 3 , label:'使用术语'},
//   { from: 1, to: 4 , label:'使用术语'},
//   { from: 5, to: 2 , label:'编码' },
//   { from: 6, to: 5, label:'编码规则'},
// ]);

const nodes = new DataSet([
  { id: 1, label: '基本信息', color:'pink', shape:'circle' },
  { id: 2, label: '性别' , color:'green', shape:'box'},
  { id: 21, label: '男性' , color:'grey', shape:'box'},
  { id: 3, label: '民族', color:'green', shape:'box'},
  { id: 31, label: '藏族', color:'grey', shape:'box'},
  { id: 4, label: '年龄', color:'green', shape:'box'},
  { id: 41, label: '76', color:'grey', shape:'text'},
  { id: 411, label: '年', color:'grey', shape:'box'},
  { id: 5, label: '既往史', color:'pink', shape:'circle' },
  { id: 6, label: '过往病程' , color:'green', shape:'box'},
  { id: 61, label: '便血' , color:'grey', shape:'box'},
  { id: 611, label: '入院前' , color:'grey', shape:'text'},
  { id: 612, label: '无' , color:'blue', shape:'text'},
  { id: 7, label: '过往病程' , color:'green', shape:'box'},
  { id: 71, label: '淤斑' , color:'grey', shape:'box'},
  { id: 8, label: '过往病程' , color:'green', shape:'box'},
  { id: 81, label: '便血' , color:'grey', shape:'box'},
  { id: 9, label: '补充信息' , color:'green', shape:'box'},

]);

// create an array with edges
const edges = new DataSet([
  { from: 2, to: 1, label:'属于', arrows: 'to'},
  { from: 2, to: 21, label:'值', arrows: 'to'},
  { from: 3, to: 1, label:'属于', arrows: 'to'},
  { from: 3, to: 31, label:'值', arrows: 'to'},
  { from: 4, to: 1, label:'属于', arrows: 'to'},
  { from: 4, to: 41, label:'值', arrows: 'to'},
  { from: 411, to: 41, label:'量纲', arrows: 'to'},
  { from: 2, to: 1, label:'属于', arrows: 'to'},
  { from: 6, to: 5, label:'属于', arrows: 'to'},
  { from: 7, to: 5, label:'属于', arrows: 'to'},
  { from: 8, to: 5, label:'属于', arrows: 'to'},
  { from: 9, to: 5, label:'属于', arrows: 'to'},
  { from: 61, to: 6, label:'症状', arrows: 'to'},
  { from: 611, to: 61, label:'发生于', arrows: 'to'},
  { from: 612, to: 61, label:'诱因', arrows: 'to'},
  { from: 71, to: 7, label:'症状', arrows: 'to'},
  { from: 81, to: 8, label:'症状', arrows: 'to'},
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