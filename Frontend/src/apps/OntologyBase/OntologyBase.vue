<template>
  <v-app theme="dark">
    <v-main>
      <v-row>
        <v-app-bar-nav-icon icon="mdi-arrow-left-thick" @click="back_to_HomePage"
          class="mt-10 ms-10" style="position: absolute;"></v-app-bar-nav-icon>
      </v-row>
      <v-container style="position: relative; top: 20vh;">
        <v-row>
          <HeadBanner></HeadBanner>
        </v-row>
        <v-row>
          <SearchBar></SearchBar>
        </v-row>
        <v-row justify="center">
          <ShortCut></ShortCut>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
// Import any necessary modules or components
import { useRouter } from 'vue-router';
import HeadBanner from '@/apps/OntologyBase/HeadBanner.vue';
import SearchBar from '@/apps/OntologyBase/SearchBar.vue';
import ShortCut from '@/apps/OntologyBase/ShortCut.vue'

// Define your component's data using ref
// const myData = ref('Hello, Vue 3!');
const router = useRouter();
const back_to_HomePage = () => {
  router.push({
    name: 'HomePage',
  });
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>
