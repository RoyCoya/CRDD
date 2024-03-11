<template>
    <v-col v-for="(shortcut, i) in shortcuts" :key="i" cols="auto" class="text-center">
        <v-card :href="shortcut.href" class="pa-4" rel="noopener noreferer" target="_blank" width="112" flat>
            <v-avatar :icon="shortcut.icon" class="mb-2" color="white" variant="tonal"></v-avatar>
            <div class="text-caption text-truncate" v-text="shortcut.title"></div>
        </v-card>
    </v-col>

    <v-col cols="auto" class="text-center">
        <v-dialog v-model="dialog" max-width="500">
            <template v-slot:activator="{ props }">
                <v-card v-bind="props" class="pa-4" width="112" flat>

                    <v-avatar class="mb-2" color="white" icon="mdi-plus" variant="tonal"></v-avatar>

                    <div class="text-caption text-truncate">Add shortcut</div>
                </v-card>
            </template>

            <v-card rounded="lg" title="Add shortcut">

                <template v-slot:text>
                    <v-label class="text-caption">Name</v-label>

                    <v-text-field density="compact" variant="solo-filled" flat></v-text-field>

                    <v-label class="text-caption">URL</v-label>

                    <v-text-field density="compact" variant="solo-filled" flat></v-text-field>
                </template>

                <div class="py-4 px-5 text-end">
                    <v-btn class="text-none me-2" color="blue" text="Cancel" variant="text" border
                        @click="dialog = false"></v-btn>

                    <v-btn class="text-none" color="blue" text="Done" variant="flat" @click="dialog = false"></v-btn>
                </div>
            </v-card>
        </v-dialog>
    </v-col>
</template>

<script setup>
// Import any necessary modules or components
import { ref } from 'vue';

// Define your component's data using ref
// const myData = ref('Hello, Vue 3!');
const shortcuts = [
    {
        icon: 'mdi-github',
        title: 'Master ',
        href: 'https://github.com/vuetifyjs/vuetify',
    },
    {
        icon: 'mdi-github',
        title: 'Dev',
        href: 'https://github.com/vuetifyjs/vuetify/tree/dev',
    },
    {
        icon: 'mdi-github',
        title: 'Stable',
        href: 'https://github.com/vuetifyjs/vuetify/tree/v2-stable',
    },
    {
        icon: 'mdi-github',
        title: 'My Pull Requests',
        href: 'https://github.com/vuetifyjs/vuetify/pulls/johnleider',
    },
]
const dialog = ref(false)
</script>

<style scoped>
/* Your scoped styles go here */
</style>