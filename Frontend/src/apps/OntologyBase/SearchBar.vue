<template>
  <v-col cols="12">
    <v-combobox v-model="queryString" @keyup.enter="searchOntology" :items="items" :autofocus="true"
      no-data-text="未找到相关本体" class="mx-auto pt-6" density="comfortable" menu-icon="" placeholder="本体名、ID、相关信息……"
      prepend-inner-icon="mdi-magnify" style="max-width: 700px; min-width:300px" theme="light" variant="solo" item-props
      rounded></v-combobox>
  </v-col>
</template>

<script setup>
// Import any necessary modules or components
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'

// Define your component's data using ref
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const router = useRouter();
const queryString = ref(route.query.onto_name);
const items = ref([
  '本体 1', '本体 2'
])

const searchOntology = () => {
  router.push({
    name: 'Ontology_SearchResults',
    query: {
      onto_name: queryString.value,
    },
  });
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>