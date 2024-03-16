<template>
    <v-app>
        <NavDrawer :backPage="backPage"></NavDrawer>
        <v-main>
            习题
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import NavDrawer from '@/apps/CaseBase/CaseDetails/NavDrawer.vue';


/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const backPage = 'Case_CaseBase';

/* Define your functions */
// const func_a = () => {};

</script>

<style scoped>
/* Your scoped styles go here */
</style>