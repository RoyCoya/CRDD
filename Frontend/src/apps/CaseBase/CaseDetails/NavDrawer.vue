<template>
    <v-navigation-drawer theme="dark" v-model="drawer" permanent expand-on-hover rail width="180">
        <v-list-item prepend-icon="mdi-arrow-left-thick" link @click="back_to_base"></v-list-item>

        <v-divider></v-divider>

        <v-list-item v-for="link in links" :key="link.key" :prepend-icon="link.icon" :title="link.label" :active="false"
            @click="link.nav_to" link>
        </v-list-item>
    </v-navigation-drawer>
</template>

<script setup>
/* Import any necessary modules or components */
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';


/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const router = useRouter();
const links = [
    { key: 'abstract', label: '概览', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details', params: { id: route.params.id } }) } },
    { key: 'view', label: '视图', icon: 'mdi-view-dashboard', nav_to: () => { router.push({ name: 'Case_Details_View', params: { id: route.params.id } }) } },
    { key: 'quiz', label: '习题', icon: 'mdi-puzzle', nav_to: () => { router.push({ name: 'Case_Details_Quiz', params: { id: route.params.id } }) } },
    { key: 'developing', label: '# 备用', icon: 'mdi-hammer-wrench', nav_to: null },
    //['mdi-text-box-edit', '编辑概览'],
    //['mdi-view-dashboard-edit', '编辑视图'],
    //['mdi-text-box-edit-outline', '编辑习题'],
];
const drawer = ref(true);

/* Define your functions */
// const func_a = () => {};
const back_to_base = () => {
    router.push({
        name: 'Case_CaseBase',
    });
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>