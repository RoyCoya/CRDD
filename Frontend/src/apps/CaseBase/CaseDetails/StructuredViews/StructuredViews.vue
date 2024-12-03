<template>
    <v-sheet elevation="5" class="h-100">
        <v-tabs density="compact" v-model="tab" bg-color="light" color="primary">
                <v-tab value="InfoView">信息模板</v-tab>
                <v-tab value="TreeView">树状图</v-tab>
                <v-tab value="TimelineView">时间线</v-tab>
                <v-tab value="RelationshipView">关系网</v-tab>
            </v-tabs>
        <v-container>
            <v-tabs-window v-model="tab">
                <v-tabs-window-item value="InfoView">
                    <InfoView></InfoView>
                </v-tabs-window-item>
                <v-tabs-window-item value="TreeView">
                    <TreeView></TreeView>
                </v-tabs-window-item>
                <v-tabs-window-item value="TimelineView">
                    <TimelineView></TimelineView>
                </v-tabs-window-item>
                <v-tabs-window-item value="RelationshipView">
                    <RelationView></RelationView>
                </v-tabs-window-item>
            </v-tabs-window>
        </v-container>
    </v-sheet>
</template>

<script setup>
/* Import */
import { ref } from 'vue';
import InfoView from '@/apps/CaseBase/CaseDetails/StructuredViews/InfoView/InfoView.vue';
import TreeView from '@/apps/CaseBase/CaseDetails/StructuredViews/TreeView/TreeView.vue';
import TimelineView from '@/apps/CaseBase/CaseDetails/StructuredViews/TimelineView/TimelineView.vue';
import RelationView from '@/apps/CaseBase/CaseDetails/StructuredViews/RelationView/RelationView.vue';

/* Data */
const tab = ref(null);
/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>
