<template>
    <v-app>
        <NavDrawer :backPage="backPage" :backPage_params="backPage_params"></NavDrawer>
        <v-main>
            <v-container class="pa-2" fluid>
                <v-row>
                    <v-col>
                        <PatientInfo></PatientInfo>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4">
                        <OriginRecords></OriginRecords>
                    </v-col>
                    <v-col cols="8">
                        <v-sheet elevation="5" rounded class="py-3 px-5" min-height="70vh">
                            <h2>人体图</h2>
                        </v-sheet></v-col>
                </v-row>

            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import NavDrawer from '@/apps/CaseBase/CaseDetails/NavDrawer.vue';
import PatientInfo from '@/apps/CaseBase/CaseDetails/CaseView/PatientInfo/PatientInfo.vue';
import OriginRecords from '@/apps/CaseBase/CaseDetails/CaseView/OrginRecords/OriginRecords.vue';
import { useRoute } from 'vue-router';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const backPage = 'Case_Details_View';
const backPage_params = { id: route.params.id };

/* Define your functions */
// const func_a = () => {};
</script>

<style scoped>
/* Your scoped styles go here */
</style>