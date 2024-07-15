<template>
    <v-sheet elevation="5" class="h-100">
        <v-tabs density="compact" v-model="tab" bg-color="light" color="primary">
                <v-tab value="Quiz">习题测验</v-tab>
                <v-tab value="LLMChat">问答助手</v-tab>
                <v-tab value="KnowledgeSearching">知识搜索</v-tab>
            </v-tabs>
        <v-container>
            <v-tabs-window v-model="tab">
                <v-tabs-window-item value="Quiz">
                    <CaseQuiz></CaseQuiz>
                </v-tabs-window-item>
                <v-tabs-window-item value="LLMChat">
                    <LLMChat></LLMChat>
                </v-tabs-window-item>
                <v-tabs-window-item value="KnowledgeSearching">
                    <KnowledgeSearching></KnowledgeSearching>
                </v-tabs-window-item>
            </v-tabs-window>
        </v-container>
    </v-sheet>
</template>

<script setup>
/* Import */
import { ref } from 'vue';
import CaseQuiz from '@/apps/CaseBase/CaseDetails/LearningPanel/Tabs/CaseQuiz.vue';
import LLMChat from '@/apps/CaseBase/CaseDetails/LearningPanel/Tabs/LLMChat.vue';
import KnowledgeSearching from '@/apps/CaseBase/CaseDetails/LearningPanel/Tabs/KnowledgeSearching.vue';
/* Data */
const tab = ref(null);
/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>