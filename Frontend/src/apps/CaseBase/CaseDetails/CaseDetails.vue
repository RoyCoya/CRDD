<template>
    <v-app>
        <NavDrawer :backPage="backPage"></NavDrawer>
        <v-main>
            <v-container class="ms-1" fluid>
                <v-row>
                    <v-col>
                        <PatientInfo></PatientInfo>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="3">
                        <OriginRecords></OriginRecords>
                    </v-col>
                    <v-col cols="6">
                        <StructuredViews></StructuredViews>
                    </v-col>
                    <v-col cols="3">
                        <LearningPanel></LearningPanel>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import NavDrawer from '@/apps/CaseBase/CaseDetails/NavDrawer.vue';
import PatientInfo from '@/apps/CaseBase/CaseDetails/PatientInfo/PatientInfo.vue';
import OriginRecords from '@/apps/CaseBase/CaseDetails/OrginRecords/OriginRecords.vue';
import StructuredViews from '@/apps/CaseBase/CaseDetails/StructuredViews/StructuredViews.vue';
import LearningPanel from '@/apps/CaseBase/CaseDetails/LearningPanel/LearningPanel.vue';
import { ref } from 'vue';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const backPage = 'Case_CaseBase';
const tab = ref(null);
/* Define your functions */
// const func_a = () => {};

</script>

<style scoped>
/* Your scoped styles go here */
</style>