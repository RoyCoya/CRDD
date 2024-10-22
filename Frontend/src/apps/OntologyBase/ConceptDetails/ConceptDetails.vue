<template>
    <v-app>
        <v-main>
            <AppBar :backPage="backPage" :backPage_query="backPage_query"></AppBar>
            <v-container>
                <v-row>
                    <template v-if="concept">
                        <v-col cols="12">
                            <h1 v-if="prefer_terms">{{ prefer_terms.join(" | ") }}</h1>
                            <v-progress-circular v-else indeterminate color="primary"></v-progress-circular>
                        </v-col>
                        <v-col cols="12">
                            <v-tabs v-model="tab" bg-color="black">
                                <v-tab value="BaseDefinition">基础定义</v-tab>
                                <v-tab value="TreeRelation">上下位关系</v-tab>
                                <v-tab value="GraphRelation">语义关系</v-tab>
                            </v-tabs>
                        </v-col>
                        <v-col cols="12">
                            <v-tabs-window v-model="tab">
                                <v-tabs-window-item value="BaseDefinition">
                                    <BaseDefinition :concept="concept"></BaseDefinition>
                                </v-tabs-window-item>
                                <v-tabs-window-item value="TreeRelation">
                                    <TreeRelation :concept="concept"></TreeRelation>
                                </v-tabs-window-item>
                                <v-tabs-window-item value="GraphRelation">
                                    <GraphRelation :concept="concept"></GraphRelation>
                                </v-tabs-window-item>
                            </v-tabs-window>
                            
                        </v-col>
                    </template>
                    <template v-else>
                        <!-- TODO: 垂直居中 -->
                        <v-progress-circular indeterminate color="primary"></v-progress-circular>
                    </template>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import */
import AppBar from '@/apps/OntologyBase/AppBar.vue';
import BaseDefinition from '@/apps/OntologyBase/ConceptDetails/BaseDefinition.vue';
import GraphRelation from '@/apps/OntologyBase/ConceptDetails/GraphRelation.vue';
import TreeRelation from '@/apps/OntologyBase/ConceptDetails/TreeRelation.vue';
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { retrieve } from '@/apps/OntologyBase/ConceptDetails/concept';
import { getPreferTermList } from '@/apps/OntologyBase/ConceptDetails/concept';

/* Data */
const route = useRoute();
const router = useRouter();
const backPage = ref('Ontology_SearchResults')
const backPage_query = ref({
    representation: route.query.representation,
})
const concept = ref(null);
const tab = ref("BaseDefinition")
const prefer_terms = ref(null)

/* Functions */
const fetchData = async () => {
    let result = await retrieve(route.params.id);
    if (result.status !== 200) {
        alert(result.data.message);
        router.push({
            name: backPage.value,
            query: backPage_query.value,
        });
        return;
    }
    concept.value = result.data[0];
    prefer_terms.value = await getPreferTermList(concept.value);
}

/* Define things you need to do on mounted */
onMounted(() => {
    fetchData();
});
</script>

<style scoped>
/* Your scoped styles go here */
</style>