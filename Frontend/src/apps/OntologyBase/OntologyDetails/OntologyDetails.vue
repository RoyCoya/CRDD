<template>
    <v-app>
        <v-main>
            <AppBar :backPage="backPage" :backPage_query="backPage_query" :ontology_name="ontology_name"></AppBar>
            <v-container>
                <h1>{{ ontology_name }}</h1>
                <v-divider class="mb-5"></v-divider>
                <p class="mb-5">详情描述</p>
                <v-row>
                    <RelatedResults></RelatedResults>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import { useRoute } from 'vue-router';
import { ref } from 'vue';
import AppBar from '@/apps/OntologyBase/AppBar.vue';
import RelatedResults from '@/apps/OntologyBase/OntologyDetails/RelatedResults.vue';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const ontology_name = ref('本体' + route.params.id)
const backPage = ref('Ontology_SearchResults')
const backPage_query = ref({
    onto_name: ontology_name.value,
})

/* Define your functions */
// const func_a = () => {};
</script>

<style scoped>
/* Your scoped styles go here */
</style>