<template>
    <v-container>
        <v-sheet class="pt-3">
            <v-row>
                <v-col cols="12">
                    <v-list lines="one" border="opacity-100 md primary">
                        <v-list-item class="pb-3" v-for="(message, index) in messages" :key="index" :title="message.from"
                            :subtitle="message.time">
                            {{ message.text }}
                        </v-list-item>
                    </v-list> 
                </v-col>
            </v-row>
            <v-row>
                <v-col cols="9" class="text-center">
                    <v-text-field :label="label" variant="outlined" density="compact" clearable></v-text-field>
                </v-col>
                <v-col cols="3" class="text-center">
                    <v-btn @click="" color="primary">提交</v-btn>
                </v-col>
            </v-row>
        </v-sheet>
    </v-container>
</template>

<script setup>
/* Import */
import { ref } from 'vue';
/* Data */
const messages = ref([
    { from: '用户', text: '你好！请问双下肢无水肿具体要怎么判断？', time: '10:00 AM' },
    { from: 'LLM', text: `1. 观察双侧下肢是否有明显肿胀或形态异常。
2. 轻轻按压脚踝或小腿，观察是否留下明显的指压痕或凹陷。
3. 注意突然的体重增加是否伴随腿部或脚部的肿胀。
4. 如果有症状如皮肤紧张、疼痛或红肿，可能是水肿的表现。`, time: '10:01 AM' },
    { from: '用户', text: `在这个案例里为什么要确认是否有下肢水肿？`, time: '10:02 AM' },
    { from: 'LLM', text: `1. 全面评估患者情况： 下肢水肿是体液潴留的一个常见体征，可能提示心脏、肾脏或肝脏等器官功能异常。这对于全面评估患者的整体健康状况非常重要。
2. 诊断和鉴别诊断的重要参考： 下肢水肿可以是多种疾病的表现，包括心血管疾病、肾脏疾病或淋巴系统问题等。这些疾病可能与患者当前的病理情况有关，或者对其治疗...`, time: '10:03 AM' },
])
/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>