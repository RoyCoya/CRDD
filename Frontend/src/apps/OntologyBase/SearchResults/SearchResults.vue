<template>
    <v-app>
        <v-main class="bg-grey-lighten-3">
            <AppBar :backPage="backPage"></AppBar>
            <v-container style="max-width: 1500px;">
                <v-row>
                    <v-col cols="8">
                        <h2>搜索结果</h2>
                        <ResultsList></ResultsList>
                    </v-col>
                    <v-col cols="4">
                        <h2>相关内容</h2>
                        <RelatedResults></RelatedResults>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
// Import any necessary modules or components
import { ref } from 'vue';
import AppBar from '@/apps/OntologyBase/AppBar.vue';
import ResultsList from '@/apps/OntologyBase/SearchResults/ResultsList.vue';
import RelatedResults from '@/apps/OntologyBase/OntologyDetails/RelatedResults.vue';

// Define your component's data using ref
// const myData = ref('Hello, Vue 3!');
const backPage = ref('Ontology_OntologyBase')
</script>

<style scoped>
/* Your scoped styles go here */
</style>