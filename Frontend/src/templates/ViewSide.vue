<template>
    <v-sheet elevation="5" rounded class="py-3 px-5" min-height="70vh">
        <v-row>
            <v-col cols="9">
                <h2>展览板</h2>
            </v-col>
            <v-col cols="3"><v-select label="视图" v-model="view_selected" :items="views" item-title="label"
                    item-value="view" return-object persistent-hint variant="outlined"
                    density="compact"></v-select></v-col>
        </v-row>
        <v-row>
            <v-col>
                <component :is="view_selected.component"></component>
            </v-col>
        </v-row>
    </v-sheet>
</template>

<script setup>
/* Import any necessary modules or components */
import { ref } from 'vue';
import InfoView from '@/apps/CaseBase/CaseDetails/CaseView/ViewSide/InfoView.vue';
import RelationView from '@/apps/CaseBase/CaseDetails/CaseView/ViewSide/RelationView.vue';
import TimelineView from '@/apps/CaseBase/CaseDetails/CaseView/ViewSide/TimelineView.vue';
import BodyView from '@/apps/CaseBase/CaseDetails/CaseView/ViewSide/BodyView.vue';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const views = [
    { view: 'info', label: '重点信息', component: InfoView },
    { view: 'relation', label: '关系网', component: RelationView },
    { view: 'timeline', label: '时间线', component: TimelineView },
    { view: 'body', label: '人体图', component: BodyView },
]

// const views = [
//     {key: 'InfoView', title: '重点信息', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Info', params: { id: route.params.id } }) }},
//     {key: 'RelationView', title: '关系网', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Relation', params: { id: route.params.id } }) }},
//     {key: 'TimelineView', title: '时间线', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Timeline', params: { id: route.params.id } }) }},
//     {key: 'BodyView', title: '人体图', icon: 'mdi-text-box', nav_to: () => { router.push({ name: 'Case_Details_View_Body', params: { id: route.params.id } }) }},
// ];
const view_selected = ref(views[0])

/* Define your functions */
// const func_a = () => {};
</script>

<style scoped>
/* Your scoped styles go here */
</style>