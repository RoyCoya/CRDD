<template>
    <v-container>
        <v-hover v-for="concept in concepts" :key="concept.element_id">
            <template v-slot:default="{ isHovering, props}">
                <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" class="mb-5"
                    @click="navToDetails(concept.element_id)">
                    <v-list-item lines="two" rounded>
                        <v-list-item-title>
                            <span v-if="concept.prefer_terms">{{ concept.prefer_terms.join(" | ") }}</span>
                            <span v-else><v-progress-circular indeterminate color="primary"></v-progress-circular></span>
                        </v-list-item-title>
                        <v-list-item-subtitle class="text-truncat">
                            ID: {{ concept.element_id }}
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-card>
            </template>
        </v-hover>
    </v-container>
</template>

<script setup>
/* Import any necessary modules or components */
import { useRouter, useRoute } from 'vue-router';
import { getPreferTermList } from '@/apps/OntologyBase/ConceptDetails/concept';
import { onMounted, ref } from 'vue';
const route = useRoute();
const router = useRouter();

const props = defineProps({
    concepts: {
        type: Array,
        required: true
    },
});

const concepts =ref(props.concepts)

/* Define your functions */
// const func_a = () => {};
const navToDetails = (id) => {
    router.push({
        name: 'Ontology_Details',
        params: {
            id: id,
        },
        query: {
            representation: route.query.representation
        }
    })
};

const fetchData = async(concept) => {
    concept.prefer_terms = await getPreferTermList(concept);
}

onMounted(() => {
    concepts.value.forEach(concept => {
        fetchData(concept)
    });
});
</script>

<style scoped>
/* Your scoped styles go here */
</style>