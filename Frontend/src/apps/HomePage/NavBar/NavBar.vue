<template>
    <v-app-bar flat theme="dark">
        <v-container class="mx-auto d-flex align-center justify-center">
            <v-avatar class="me-4 " color="grey-darken-1" size="32"></v-avatar>
            <div v-for="link in links" :key="link.name">
                <template v-if="linkRoute = routes.find(route => route.name === link.name)">
                    <v-btn :to="linkRoute.path" :text="link.title" variant="text" class="me-5"></v-btn>
                </template>
            </div>

            <v-spacer></v-spacer>

            <v-responsive max-width="160">
                <v-text-field density="compact" label="全局搜索" rounded="lg" variant="solo-filled" flat hide-details
                    single-line></v-text-field>
            </v-responsive>
            <v-btn :to="routes.find(route => route.name === 'HomePage_login')" variant="text" class="ms-5">登录</v-btn>
        </v-container>
    </v-app-bar>
</template>

<script setup>
import { routes } from '@/configs/router/router';

const links = [
    { title: '主页', name: 'HomePage' },
    { title: '案例库', name: 'Case_CaseBase' },
    { title: '本体库', name: 'Ontology_OntologyBase' },
    { title: 'AI库', name: 'AI_AIBase' },
    { title: '语料库', name: 'Courpus_CorpusBase' },
];
</script>

<style></style>@/configs/router/router