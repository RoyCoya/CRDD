<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <v-card class="pa-3" border>
                    {{ question }}
                </v-card>
            </v-col>
        </v-row>
        <v-form class="pt-3" validate-on="submit lazy" @submit.prevent="submit">
            <v-textarea :label="label" variant="outlined" clearable></v-textarea>
            <v-row>
                <v-col cols="6">
                    <v-btn @click="">上一题</v-btn>
                </v-col>
                <v-col cols="6" class="text-right">
                    <v-btn @click="" color="primary">下一题</v-btn>
                </v-col>
            </v-row>
        </v-form>
        <v-row>
            <v-col cols="12">
                <v-card class="pa-3" border>
                    <p class="px-4"><span class="text-success">参考答案：</span><span v-html="answer"></span>
                    </p>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
/* Import */
import { ref } from 'vue'
const question = "13.双下肢无水肿对于判断患者的全身状况有什么帮助？"
const rules = [value => checkApi(value)]
const label = "作答"
const loading = ref(false)
const userName = ref('')
const answer = ref(`<ol>
        <li>
            <strong>评估心功能</strong>：
            <ul>
                <li><strong>意义</strong>：下肢水肿是心功能不全（尤其是右心衰竭）的常见表现。双下肢无水肿提示患者目前没有明显的心力衰竭，特别是右心衰竭的表现。</li>
                <li><strong>临床判断</strong>：结合患者心肺听诊无异常，可以排除明显的心脏疾病导致的下肢水肿。</li>
            </ul>
        </li>
        <li>
            <strong>评估肾功能</strong>：
            <ul>
                <li><strong>意义</strong>：肾脏疾病，特别是肾病综合征和慢性肾功能衰竭，常伴有全身性水肿。双下肢无水肿提示患者目前肾功能可能正常，或者肾脏疾病未导致明显的水钠潴留。</li>
                <li><strong>临床判断</strong>：这有助于排除肾脏原因引起的下肢水肿，并减少对肾病相关治疗的误诊。</li>
            </ul>
        </li>
        <li>
            <strong>评估肝功能</strong>：
            <ul>
                <li><strong>意义</strong>：肝硬化和肝功能衰竭患者常有低蛋白血症，导致腹水和下肢水肿。双下肢无水肿提示患者可能没有严重的肝功能障碍。</li>
                <li><strong>临床判断</strong>：结合无黄染和肝脾未触及肿大，可以进一步排除肝脏疾病作为主要病因。</li>
            </ul>
        </li>
        <li>
            <strong>评估静脉回流</strong>：
            <ul>
                <li><strong>意义</strong>：静脉回流障碍，如深静脉血栓形成或慢性静脉功能不全，常导致下肢水肿。双下肢无水肿提示没有明显的静脉回流受阻。</li>
                <li><strong>临床判断</strong>：帮助排除静脉回流障碍相关疾病，减少对血管外科干预的误诊。</li>
            </ul>
        </li>
        <li>
            <strong>评估营养状况</strong>：
            <ul>
                <li><strong>意义</strong>：营养不良，特别是低蛋白血症，可导致水肿。双下肢无水肿提示患者的营养状况可能良好或没有严重的低蛋白血症。</li>
                <li><strong>临床判断</strong>：结合其他体格检查和实验室结果，进一步评估患者的营养和代谢状态。</li>
            </ul>
        </li>
    </ol>`)

async function submit(event) {
    loading.value = true
    const results = await event
    loading.value = false
    alert(JSON.stringify(results, null, 2))
}

let timeout = -1
async function checkApi(userName) {
    return new Promise(resolve => {
        clearTimeout(timeout)

        timeout = setTimeout(() => {
            if (!userName) return resolve('Please enter a user name.')
            if (userName === 'johnleider') return resolve('User name already taken. Please try another one.')
            return resolve(true)
        }, 1000)
    })
}
/* Data */

/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>