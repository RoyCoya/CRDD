<template>
    <v-app>
        <NavDrawer :backPage="backPage"></NavDrawer>
        <v-main>
            <v-container class="pa-2" fluid>
                <v-row>
                    <v-col v-for="view in views" :key="view.key">
                        <v-card :title="view.title" :prepend-icon="view.icon" @click="view.nav_to" link>
                            
                        </v-card>
                    </v-col>
                </v-row>
                <v-row class="mt-1">
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import NavDrawer from '@/apps/CaseBase/CaseDetails/NavDrawer.vue';
import { useRoute, useRouter } from 'vue-router';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const router = useRouter();
const views = [
    {key: 'InfoView', title: '重点信息', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Info', params: { id: route.params.id } }) }},
    {key: 'RelationView', title: '关系网', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Relation', params: { id: route.params.id } }) }},
    {key: 'TimelineView', title: '时间线', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Timeline', params: { id: route.params.id } }) }},
    {key: 'BodyView', title: '人体图', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Body', params: { id: route.params.id } }) }},
];
const backPage = 'Case_CaseBase';

/* Define your functions */
// const func_a = () => {};
</script>

<style scoped>
/* Your scoped styles go here */
</style>