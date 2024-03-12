<template>
    <v-app>
        <v-navigation-drawer theme="dark" v-model="drawer" expand-on-hover rail width="180">
            <v-list-item prepend-icon="mdi-arrow-left-thick" link @click="back_to_base"></v-list-item>

            <v-divider></v-divider>

            <v-list-item v-for="(link, index) in links" :key="link[0]" :prepend-icon="link[0]" :title="link[1]"
                :active="index === 0" link>
            </v-list-item>
        </v-navigation-drawer>

        <v-main>
            <v-container class="pa-2" fluid>
                <v-card elevation="5">
                    <v-sheet class="px-5 pt-3 text-body-2">
                        <v-row align="center">
                            <v-col cols="1">姓名：xxx</v-col>
                            <v-col cols="1">性别：男</v-col>
                            <v-col cols="1">年龄：76</v-col>
                            <v-col cols="1">民族：藏族</v-col>
                            <v-col cols="8">诊断结果（ICD）：

                                <v-chip size="small" variant="elevated" class="me-1">
                                    <v-tooltip location="bottom" activator="parent" text="D46.900"></v-tooltip>
                                    骨髓增生异常肿瘤
                                </v-chip>

                                <v-chip size="small" variant="elevated" class="me-1">
                                    <v-tooltip location="bottom" activator="parent" text="C92.000"></v-tooltip>
                                    急性髓系白血病
                                </v-chip>

                            </v-col>
                        </v-row>
                        <v-row align="center">
                            <v-col cols="3">现病史：
                                <v-chip size="small" variant="elevated" class="me-1">
                                    <v-tooltip location="bottom" activator="parent" text="K92.1"></v-tooltip>
                                    便血
                                </v-chip>
                            </v-col>
                            <v-col cols="3">既往史：</v-col>
                            <v-col cols="2">个人史：</v-col>
                            <v-col cols="2">家族史：无</v-col>
                            <v-col cols="2">过敏史：无</v-col>

                        </v-row>
                    </v-sheet>
                    <v-card-actions class="d-flex justify-end">
                        <v-btn variant="tonal" size="small" @click="reveal_patient_info = true"
                            color="grey-darken-1">查看所有
                            >>></v-btn>
                    </v-card-actions>
                </v-card>
                <v-row class="mt-1">
                    <v-col cols="6">
                        <v-sheet elevation="5" rounded class="pa-3" min-height="70vh">
                            <v-row>
                                <v-col cols="9">
                                    <h2 class="mb-3">伴DDX41胚系突变骨髓增生异常肿瘤/急性髓系白血病1例</h2>
                                </v-col>
                                <v-col class="d-flex justify-end">
                                    <v-switch density="compact" :model-value="true" color="primary" label="显示标注"></v-switch>
                                </v-col>
                            </v-row>
                            
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;患者，男性，藏族，76 岁，入院前 16 年余无明显诱因出现便后出血，约 1 d
                                后可自行
                                停止，未予重视。入院前 8 年开始出现磕碰处瘀斑，未予治疗。病程中间断便血，持续时
                                间逐渐延长，便血次数逐渐增多，未系统诊治。入院前 1 年上述症状加重。血常规：Hb
                                107 g/L，RBC 2.93×1012/L，MCV 106.7 fl，WBC 1.94×109/L，Gran% 34.2%，Lym%
                                60.6%，Mon% 1.5%，PLT 44×109/L。</p>
                            <v-divider class="mb-3"></v-divider>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;体格检查：神志清楚，体格检查合作，全身皮肤未见瘀点、瘀斑及皮下出血点，可见
                                散在陈旧性皮疹，双下肢色素沉着，皮肤、巩膜无黄染，全身浅表淋巴结未触及肿大。胸
                                骨无压痛。双肺呼吸音清，未闻及干湿性啰音，律齐，各瓣膜未闻及病理性杂音。全腹
                                软，无压痛及反跳痛。肝脾肋下未触及。双下肢无水肿。
                            </p>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;诊断方法： 运用 HE
                                染色、免疫组化、流式免疫分型、染色体核型分析、分子生物学（实时
                                荧光定量 PCR+二代测序）进行诊断及鉴别诊断并分析讨论，血液病理综合诊断为：1.骨髓
                                增生异常肿瘤/急性髓系白血病；2.具有胚系易感性的髓系肿瘤（DDX41 基因突变），无预
                                先存在的血小板疾病或器官功能障碍。</p>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;诊断：
                                综合 C-MICM 诊断：MDS/AML 伴 ASXL1、SRSF2、TP53、DDX41（双位点）一级突
                                变，提示预后不良，DDX41 的 exon6 c.484del 为胚系突变，具有一定遗传易感性。2022 年
                                国际共识分类（ICC）根据对血液系统恶性肿瘤生物学的最新进展将髓系肿瘤重新分类，其
                                中原始细胞为 10%~19%的骨髓增生异常肿瘤（MDS）被归类为 MDS/急性髓系白血病
                                （AML）</p>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;鉴别诊断：MDS/AML 需要鉴别的是 MDS 和
                                AML，据骨髓涂片及流式免疫分型原始细胞计数均
                                小于 20%，不足以诊断 AML，骨髓活检原始细胞可能已超过 20%，可以诊断 AML，但患
                                者起病缓慢，且有皮肤瘀斑病史 8 年，诊断 MDS/AML 更为合适。原始细胞计数为
                                10%~19%的 MDS 病例现在被诊断为 MDS/AML，这反映了 AML 和 MDS 之间的诊断连续
                                性以及原始细胞计数较低的个体患者的临床和遗传异质性</p>
                            <v-divider class="mb-3"></v-divider>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;治疗方法：2023 年6 月 16 日予阿扎胞苷 100 mg d1~7
                                方案行第 1 周期化疗，辅以护胃、升
                                细胞、改善贫血等支持治疗，化疗过程顺利。病程中患者诉全身散在红色皮疹及皮下结节
                                伴瘙痒不适，考虑斯威特综合征可能性大，予甲泼尼龙抗炎，复方氟米松软膏对症止痒，
                                病情好转后出院。</p>
                            <p class="mb-3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;临床转归：患者自化疗后，症状及血常规明显改善，精神可，饮食、睡眠可，大小便正常，
                                体重未见明显增减。</p>
                        </v-sheet>
                    </v-col>
                    <v-col cols="6">
                        <v-sheet elevation="5" rounded class="pa-3" min-height="70vh">
                            <h2>信息视图</h2>
                        </v-sheet>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import { ref } from 'vue';
import { useRouter } from 'vue-router';


/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const router = useRouter();
const links = [
    ['mdi-view-dashboard', '视图'],
    //['mdi-view-dashboard-edit', '编辑视图'],
    ['mdi-text-box-outline', '习题'],
    //['mdi-text-box-edit-outline', '编辑习题'],
    ['mdi-hammer-wrench', '#备用'],
];
const reveal_patient_info = false;
const drawer = ref(null);

/* Define your functions */
// const func_a = () => {};
const back_to_base = () => {
    router.push({
        name: 'Case_CaseBase',
    });
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>