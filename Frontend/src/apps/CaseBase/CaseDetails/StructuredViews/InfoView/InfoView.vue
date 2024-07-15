<template>
    <v-container>
        <v-row class="align-center">
            <v-col cols="6">
                <v-select hide-details="auto" variant="solo" :items="templates" v-model="template_now" rounded=""
                    density="compact" @update:model-value="change_content(template_now)">
                </v-select>
            </v-col>
            <v-col cols="6">
                <v-btn prepend-icon="mdi-plus-circle" color="primary" rounded="pill">
                    新增模板
                </v-btn>
            </v-col>
        </v-row>
        <!-- TODO: use https://www.npmjs.com/package/unplugin-vue-markdown -->
        <v-row>
            <v-col v-html="template_content" class="px-5">

            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';
/* Import */

/* Data */
const template_now = ref('入院检查')
const templates = ref(['入院检查','阳性症状','阳性体征', '既往诊断', '既往治疗','诊断','治疗']);
const templates_value = {
    '入院检查': `<h1>基本信息</h1>
                        <p>姓名：</p>
                        <p>年龄：76</p>
                        <p>性别：男性</p>
                        <p>民族：藏族</p>
                        <hr>
                        <h1>一诉五史</h1>
                        <h2>既往史</h2>
                        <ul>
                            <li>
                                入院前16年余无明显诱因出现便后出血，约1d后可自行停止，未予重视。
                            </li>
                            <li>入院前8年开始出现磕碰处瘀斑，未予治疗。</li>
                            <li>病程中间断便血，持续时间逐渐延长，便血次数逐渐增多，未系统诊治。</li>
                            <li>入院前 1 年上述症状加重。</li>
                        </ul>
                        <h1>体格检查</h1>
<ul>
    <li>神志清楚，体格检查合作。</li>
    <li>全身皮肤未见瘀点、瘀斑及皮下出血点，可见散在陈旧性皮疹。</li>
    <li>双下肢色素沉着，皮肤、巩膜无黄染。</li>
    <li>全身浅表淋巴结未触及肿大。</li>
    <li>胸骨无压痛。</li>
    <li>双肺呼吸音清，未闻及干湿性啰音，律齐，各瓣膜未闻及病理性杂音。</li>
    <li>全腹软，无压痛及反跳痛。</li>
    <li>肝脾肋下未触及。</li>
    <li>双下肢无水肿。</li>
</ul>
`,
    '诊断': `<h1>诊断方法</h1>
<ul>
    <li>HE染色</li>
    <li>免疫组化</li>
    <li>流式免疫分型</li>
    <li>染色体核型分析</li>
    <li>分子生物学（实时荧光定量 PCR+二代测序）</li>
</ul>
<hr>
<h1>诊断</h1>
<p>血常规：</p>
<ul>
    <li>Hb 107 g/L</li>
    <li>RBC 2.93×10<sup>12</sup>/L</li>
    <li>MCV 106.7 fl</li>
    <li>WBC 1.94×10<sup>9</sup>/L</li>
    <li>Gran% 34.2%</li>
    <li>Lym% 60.6%</li>
    <li>Mon% 1.5%</li>
    <li>PLT 44×10<sup>9</sup>/L</li>
</ul>
<p>综合 C-MICM 诊断：</p>
<ul>
    <li>MDS/AML 伴 ASXL1、SRSF2、TP53、DDX41（双位点）一级突变，提示预后不良。</li>
    <li>DDX41 的 exon6 c.484del 为胚系突变，具有一定遗传易感性。</li>
</ul>
<p>2022 年国际共识分类（ICC）将原始细胞为 10%~19%的骨髓增生异常肿瘤（MDS）归类为 MDS/急性髓系白血病（AML）。</p>
<hr>
<h1>鉴别诊断</h1>
<p>MDS/AML 需要鉴别的是 MDS 和AML：</p>
<ul>
    <li>据骨髓涂片及流式免疫分型原始细胞计数均小于 20%，不足以诊断 AML。</li>
    <li>骨髓活检原始细胞可能已超过 20%，可以诊断 AML，但患者起病缓慢，且有皮肤瘀斑病史 8 年，诊断 MDS/AML 更为合适。</li>
    <li>原始细胞计数为10%~19%的 MDS 病例现在被诊断为 MDS/AML，这反映了 AML 和 MDS 之间的诊断连续性以及原始细胞计数较低的个体患者的临床和遗传异质性。</li>
</ul>`,
    '治疗': `<h1>治疗方法</h1>
<p>2023 年6 月 16 日予阿扎胞苷 100 mg d1~7方案行第 1 周期化疗，辅以护胃、升细胞、改善贫血等支持治疗，化疗过程顺利。</p>
<p>病程中患者诉全身散在红色皮疹及皮下结节伴瘙痒不适，考虑斯威特综合征可能性大，予甲泼尼龙抗炎，复方氟米松软膏对症止痒，病情好转后出院。</p>
<hr>
<h1>临床转归</h1>
<p>患者自化疗后，症状及血常规明显改善，精神可，饮食、睡眠可，大小便正常，体重未见明显增减。</p>`
}
var template_content = ref(templates_value['入院检查']);
function change_content(key) {
    template_content.value = templates_value[key]
}

/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>