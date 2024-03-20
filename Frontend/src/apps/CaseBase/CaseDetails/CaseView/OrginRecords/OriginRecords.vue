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
                <v-slider v-model="annotation_depth" :step="1" :max="5"></v-slider>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <div v-html="getAnnotatedRecords(records, props.annotations)">
                </div>
            </v-col>
        </v-row>
    </v-sheet>
</template>

<script setup>
import { ref } from 'vue';

/* Import any necessary modules or components */

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const props = defineProps({
    records: {
        type: Object,
        required: true,
    },
    annotations_type: String,
    annotations: Object,
});

const records = props.records;
const annotation_depth = ref(0);

/* Define your functions */
// const func_a = () => {};
function getAnnotatedText(record, annotation) {
    if (annotation.details) return ` <span style="background-color: blue; color: white;">${record.text.substring(annotation.start, annotation.end)}</span> `;
    else return ` <span style="background-color: red; color: white;">${record.text.substring(annotation.start, annotation.end)}</span> `;
}

function getAnnotatedRecord(record, annotations) {
    let result = record.text;
    let offset = 0;

    for (const annotation of annotations) {
        if (annotation.record_id === record.id && annotation.depth == annotation_depth.value) {
            const annotation_length = annotation.end - annotation.start;
            const annotatedText = getAnnotatedText(record, annotation);
            const start = annotation.start + offset;
            const end = annotation.end + offset
            result = result.substring(0, start) + annotatedText + result.substring(end)
            offset += annotatedText.length - annotation_length
        }
    }

    return `<p>${result}</p>`;
}

function getAnnotatedRecords(records, annotations) {
    let result = '';

    for (const record of records) {
        const annotatedRecord = getAnnotatedRecord(record, annotations);
        result += annotatedRecord + '<hr class="my-2" />';
    }

    return result;
}

</script>

<style scoped>
/* Your scoped styles go here */
</style>