<template>
    <h2>优选术语</h2>
    <!-- TODO: 美化：https://vuetifyjs.com/en/components/lists/#items -->
    <template v-if="prefer_terms">
        <ul v-if="prefer_terms.length > 0" class="ms-5">
            <li v-for="term in prefer_terms" :key="term.element_id">
                {{ term.value }}
                <span v-if="term.definition_sets">
                    &lt;--定义集--
                    <span v-for="definition_set in term.definition_sets" :key="definition_set.element_id">
                        <a v-if="Object.keys(definition_set).length > 0" href="#">
                            <span v-if="definition_set.abbreviation">
                                {{ definition_set.abbreviation }}
                            </span>
                            <span v-else>{{ definition_set.value }}</span>
                        </a>
                        <span v-else><v-progress-circular :size="20" indeterminate
                                color="primary"></v-progress-circular></span>
                    </span>
                </span>
                <span v-else>
                    <v-progress-circular :size="20" indeterminate color="primary"></v-progress-circular>
                </span>
            </li>
        </ul>
        <div v-else class="text-red-accent-4">该本体无优选术语</div>
    </template>
    <template v-else>
        <v-progress-circular :size="20" indeterminate color="primary"></v-progress-circular>
    </template>

    <v-divider class="my-5"></v-divider>

    <h2 class="mt-3">同义术语</h2>
    <template v-if="synonyms">
        <ul class="ms-5">
            <li v-for="term in synonyms" :key="term.element_id">
                {{ term.value }}
            </li>
        </ul>
    </template>
    <template v-else>
        <v-progress-circular :size="20" indeterminate color="primary"></v-progress-circular>
    </template>
</template>

<script setup>
/* Import */
import { getPreferTerms, getSynonyms, sortTerms } from '@/apps/OntologyBase/ConceptDetails/concept';
import { onMounted, ref } from 'vue';
import { retrieve } from '@/apps/OntologyBase/DefinitionSetDetails/definition_set';
/* Data */
const props = defineProps({
    concept: {
        type: Object,
        required: true
    },
});
const concept = props.concept
const prefer_terms = ref(null)
const synonyms = ref(null)

/* Functions */

/* Define things you need to do on mounted */
onMounted(async () => {
    let response = null
    // Prefer terms
    response = await getPreferTerms(concept)
    
    if (response.data) { prefer_terms.value = response.data }
    else { prefer_terms.value = [] }
    
    // Synonyms
    response = await getSynonyms(concept)
    if (response.data) { synonyms.value = sortTerms(response.data) }
    else { synonyms.value = [] }

    // Definition set info retrieve
    if (prefer_terms.value) {
        for (const term of prefer_terms.value) {
            term.definition_sets = await Promise.all(
                term.definition_sets.map(async (element_id) => {
                    let response = (await retrieve(element_id));
                    if (response.status == 200) {
                        return response.data[0]
                    }
                    // TODO: 错误显示
                    else { return {} }
                })
            );
        }
    }
    
    if (synonyms.value) {
        for (const term of synonyms.value) {
            term.definition_sets = await Promise.all(
                term.definition_sets.map(async (element_id) => {
                    let response = (await retrieve(element_id));
                    if (response.status == 200) {
                        return response.data[0]
                    }
                    // TODO: 错误显示
                    else { return {} }
                })
            );
        }
    }
});
</script>

<style scoped>
/* Your scoped styles go here */
</style>
