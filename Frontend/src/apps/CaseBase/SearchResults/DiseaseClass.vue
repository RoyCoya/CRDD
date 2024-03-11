<template>
    <h2>疾病分类</h2>
    <v-card class="mt-3">
        <v-list v-model:opened="open">
            <v-list-item prepend-icon="mdi-home" title="Home"></v-list-item>

            <v-list-group value="Users">
                <template v-slot:activator="{ props }">
                    <v-list-item v-bind="props" prepend-icon="mdi-account-circle" title="Users"></v-list-item>
                </template>

                <v-list-group value="Admin">

                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" title="Admin"></v-list-item>
                    </template>

                    <v-list-item v-for="([title, icon], i) in admins" :key="i" :title="title"
                        :value="title"></v-list-item>
                </v-list-group>

                <v-list-group value="Actions">

                    <template v-slot:activator="{ props }">
                        <v-list-item v-bind="props" title="Actions"></v-list-item>
                    </template>

                    <v-list-item v-for="([title, icon], i) in cruds" :key="i" :title="title"
                        :value="title"></v-list-item>
                </v-list-group>
            </v-list-group>
        </v-list>
    </v-card>
</template>

<script setup>
// Import any necessary modules or components
import { ref } from 'vue'

// Define your component's data using ref
// const myData = ref('Hello, Vue 3!');
const open = ref(['Users'])

const admins = [
    ['Management', 'mdi-account-multiple-outline'],
    ['Settings', 'mdi-cog-outline'],
]
const cruds = [
    ['Create', 'mdi-plus-outline'],
    ['Read', 'mdi-file-outline'],
    ['Update', 'mdi-update'],
    ['Delete', 'mdi-delete'],
]
</script>

<style scoped>
/* Your scoped styles go here */
</style>