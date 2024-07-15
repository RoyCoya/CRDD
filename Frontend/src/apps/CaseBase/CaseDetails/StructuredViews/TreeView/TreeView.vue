<template>
    <v-container>
        <v-row>
            <v-col cols="6">
                <v-sheet>
                    <v-row>
                        <v-combobox hide-details="auto" v-model="queryString" no-data-text="未找到相关内容" class="pa-3" density="compact"
                            placeholder="信息、本体、值……" prepend-inner-icon="mdi-magnify" theme="light" variant="solo"
                            item-props rounded></v-combobox>
                    </v-row>
                    <v-sheet class="border rounded-xl px-3 mt-5" min-height="100">
                        <InfoTree :config="config" :nodes_obj="nodes_obj" :nodes_array="nodes_array"></InfoTree>
                    </v-sheet>
                </v-sheet>
            </v-col>
            <v-col cols="6">

            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
/* Import any necessary modules or components */
import InfoTree from '@/apps/CaseBase/CaseDetails/StructuredViews/TreeView/SearchAndNodes.vue';
import { ref } from 'vue';
import template from '../../template';
import { getNodeText } from '@/apps/CaseBase/CaseDetails/StructuredViews/Utils/node';

/* Define your component's data using ref */

const queryString = ref(null);


// infos由后端组装。重点信息用模板做NER后再做onto锁定，锁不到的取原文
// TODO: decouple infos and annotations, wrap annation functions into js file
const infos = ref(template.information);

const nodes_obj = ref({});
const nodes_array = ref([]);
infos.value.forEach(info => {
    var prefixed_child = [];
    info.children.forEach(child => {
        prefixed_child.push('id' + child);
    })
    info.children = prefixed_child;
    info.id = 'id' + info.id
});
infos.value.forEach(info => {
    info['text'] = getNodeText(info);
    nodes_array.value.push(info);
    const { id, ...rest } = info;
    nodes_obj.value[id] = { id, ...rest, state: {} };
});
const config = ref({});
/* Define your functions */

</script>

<style scoped>
/* Your scoped styles go here */
</style>