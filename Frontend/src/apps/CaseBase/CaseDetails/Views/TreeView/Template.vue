<template>
    <v-row>
        <v-col>
            <h2>显示模板</h2>
        </v-col>
    </v-row>
    <v-row>
        <v-col cols="6">
            <v-select variant="solo" :items="templates" model-value="默认模板" rounded="" density="compact">
            </v-select>
        </v-col>
    </v-row>
    <!-- TODO: use https://www.npmjs.com/package/unplugin-vue-markdown -->
    <v-row>
        <v-col>
            <v-sheet border min-height="50vh" class="pa-3">
                <h1>基本信息</h1>
                <p>姓名：xxx</p>
                <p>年龄：76</p>
                <p>性别：男性</p>
                <hr>
                <h1>一诉五史</h1>
                <h2>既往史</h2>
                <p>入院前16年余无明显诱因出现便后出血，约1d后可自行停止，未予重视。</p>
                <p>入院前8年开始出现磕碰处瘀斑，未予治疗。</p>
                <p>病程中间断便血，持续时间逐渐延长，便血次数逐渐增多，未系统诊治。</p>
                <p>入院前 1 年上述症状加重。</p>
            </v-sheet>
        </v-col>
    </v-row>
</template>

<script setup>
import { ref } from 'vue';
/* Import */

/* Data */
const templates = ref(['默认模板']);

/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>