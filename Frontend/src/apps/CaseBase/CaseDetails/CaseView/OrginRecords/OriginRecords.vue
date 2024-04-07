<template>
    <v-sheet elevation="5" rounded class="py-3 px-5" min-height="70vh">
        <v-row>
            <v-col cols="12">
                <h2 class="mb-3">伴DDX41胚系突变骨髓增生异常肿瘤/急性髓系白血病1例</h2>
            </v-col>
            <!-- <v-col class="d-flex justify-end">
                <v-switch density="compact" :model-value="true" color="primary" label="显示标注"></v-switch>
            </v-col> -->
        </v-row>
        <v-row>
            <v-col>显示标注深度：{{ annotation_depth }}</v-col>
            <v-col>
                <v-slider v-model="annotation_depth" :step="1" :max="5" min="-1"
                    @update:modelValue="changeDepth(annotation_depth)"></v-slider>
            </v-col>
        </v-row>
        <v-row>
            <v-col @click="focusAnnotation">
                <div id="records" v-html="annotatedRecordHTML">
                </div>
            </v-col>
        </v-row>
    </v-sheet>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { emitter } from '@/apps/CaseBase/CaseDetails/CaseView/emitter';

/* Import any necessary modules or components */

/* Define your component's data using ref */
// TODO: decoupling functions to js files
const props = defineProps({
    records: {
        type: Object,
        required: true,
    },
    annotations_type: String,
    annotations: Object,
    annotation_default_color: String,
});
const records = props.records;
const annotations = props.annotations;
const annotation_depth = ref(0);
const annotation_default_color = props.annotation_default_color;
const annotatedRecordHTML = ref('')

//TODO: optimize record with annotations generation functions, try createElementBlock in vue
const getAnnotatedText = (record, annotation, focused) => {
    return focused
    ? ` <span id="anno_${annotation.id}" style="background-color: red; color: white;">${record.text.substring(annotation.start, annotation.end)}</span> `
    : ` <span id="anno_${annotation.id}" style="background-color: ${annotation.color ? annotation.color : annotation_default_color}; color: white;">${record.text.substring(annotation.start, annotation.end)}</span> `;
};

const getAnnotatedRecord = (record, annotations, focusedIDs = []) => {
    let result = record.text;
    let offset = 0;

    for (const annotation of annotations) {
        if (annotation.record_id === record.id) {
            const annotation_length = annotation.end - annotation.start;
            const focused = focusedIDs.includes(annotation.id);
            const annotatedText = getAnnotatedText(record, annotation, focused);
            const start = annotation.start + offset;
            const end = annotation.end + offset
            result = result.substring(0, start) + annotatedText + result.substring(end)
            offset += annotatedText.length - annotation_length
        }
    }

    return `<p>${result}</p>`;
};

const getAnnotatedRecordsHTML = (records, annotations, focusedIDs = []) => {
    let result = '';

    for (const record of records) {
        const annotatedRecord = getAnnotatedRecord(record, annotations, focusedIDs);
        result += annotatedRecord + '<hr class="my-2" />';
    }

    annotatedRecordHTML.value = result;
    return result;
}

const getAnnotationsByDepth = (depth) => {
    return annotations.filter(obj => obj.depth === depth);
}

const changeDepth = (depth) => {
    annotation_depth.value = depth;
    annotatedRecordHTML.value = getAnnotatedRecordsHTML(records, getAnnotationsByDepth(depth));
}

// listen annotation click
const focusAnnotation = (event) => {
    const element_id = event.target.id
    if(element_id.startsWith('anno_')){
        emitter.emit('focusAnnotation', (element_id.substring(5)));
    }
    // TODO: highlight anno and focus node on tree
} 

/* page initialization */
changeDepth(0);

onMounted(() => {
    /* info view events */
    // when focus treeview node, display brother nodes and hightlight focused node
    emitter.on('focusNodeOnTreeview', (annotationsToShow) => {
        const focusedIDs = []
        focusedIDs.push(annotationsToShow[0].id)
        annotationsToShow.sort((a, b) => a.start  - b.start)
        annotation_depth.value = annotationsToShow[0].depth;
        annotatedRecordHTML.value = getAnnotatedRecordsHTML(records, annotationsToShow, focusedIDs);
    });

    /* relation view events */
    emitter.on('blurNodeOnTreeView', () => {
        changeDepth(annotation_depth.value)
    });
});

</script>

<style scoped>
/* Your scoped styles go here */
</style>