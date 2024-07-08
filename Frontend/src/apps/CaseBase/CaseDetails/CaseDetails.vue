<template>
    <v-app>
        <NavDrawer :backPage="backPage"></NavDrawer>
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
                        <InfoTree></InfoTree>
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
import InfoTree from '@/apps/CaseBase/CaseDetails/Views/TreeView/TreeView.vue';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const backPage = 'Case_CaseBase';

/* Define your functions */
// const func_a = () => {};

</script>

<style scoped>
/* Your scoped styles go here */
</style>