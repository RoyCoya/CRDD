<template>
    <v-app>
        <v-main class="bg-grey-lighten-3">
            <AppBar :backPage="backPage"></AppBar>
            <v-container style="max-width: 1500px;">
                <v-row>
                    <v-col cols="8">
                        <h2>搜索结果</h2>
                        <div v-if="concepts">
                            <ResultsList :concepts="concepts"></ResultsList>
                        </div>
                        <div v-else><v-progress-circular indeterminate color="primary"></v-progress-circular></div>
                    </v-col>
                    <!-- <v-col cols="4">
                        <h2>相关内容</h2>
                        <RelatedResults></RelatedResults>
                    </v-col> -->
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
const route = useRoute();
const router = useRouter();
import AppBar from '@/apps/OntologyBase/AppBar.vue';
import ResultsList from '@/apps/OntologyBase/SearchResults/ResultsList.vue';
// import RelatedResults from '@/apps/OntologyBase/ConceptDetails/RelatedResults.vue';
import { search } from '@/apps/OntologyBase/ConceptDetails/concept';

const backPage = ref('Ontology_OntologyBase')
const concepts = ref(null)
const fetchData = async () => {
    let result = await search(route.query.representation);
    if (result.status !== 200) {
        alert(result.data.message);
        router.push({ name: 'Ontology_OntologyBase', });
        return;
    }
    
    concepts.value = result.data;
}

import { onMounted } from 'vue';
onMounted(() => {
    // concepts.value = result
    // route.query.representation
    fetchData();
});

</script>

<style scoped>
/* Your scoped styles go here */
</style>