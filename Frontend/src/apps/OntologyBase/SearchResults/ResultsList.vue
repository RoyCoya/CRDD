<template>
    <v-container>
        <v-hover v-for="index in 5" :key="index">
            <template v-slot:default="{ isHovering, props }">
                <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" class="mb-5"
                    @click="navToDetails(index)">
                    <v-list-item lines="two" subtitle="详细描述" :title="`本体 ${index}`" rounded></v-list-item>
                </v-card>
            </template>
        </v-hover>
    </v-container>
</template>

<script setup>
/* Import any necessary modules or components */
import { useRouter } from 'vue-router';
/* Define your component's data using ref */
const router = useRouter();

/* Define your functions */
// const func_a = () => {};
const navToDetails = (id) => {
    router.push({
        name: 'Ontology_Details',
        params: {
            id: id,
        },
    })
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>