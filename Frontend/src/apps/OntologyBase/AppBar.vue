<template>
    <v-app-bar :elevation="2" theme="dark">
        <template v-slot:prepend>
            <v-app-bar-nav-icon icon="mdi-arrow-left-thick" @click="back_to_Base"></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>
            CRDD Ontology Base 本体库
        </v-app-bar-title>

        <template v-slot:append>
            <v-row no-gutters class="me-3">
                <SearchBar></SearchBar>
            </v-row>
            <v-btn icon="mdi-heart"></v-btn>
        </template>
    </v-app-bar>
</template>

<script setup>
/* Import any necessary modules or components */
import { useRouter } from 'vue-router';
import SearchBar from '@/apps/OntologyBase/SearchBar.vue';

/* Define your component's data using ref */
const router = useRouter();
const props = defineProps({
    backPage: {
        type: String,
        required: true,
    },
    backPage_params: Object,
    backPage_query: Object,
    ontology_name: String,
});
console.log(props.backPage_query);

/* Define your functions */
const back_to_Base = () => {
    router.push({
        name: props.backPage,
        params: props.backPage_params,
        query: props.backPage_query
    });
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>