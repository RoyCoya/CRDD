<template>
    <v-app>
        <NavDrawer :backPage="backPage" :backPage_params="backPage_params"></NavDrawer>
        <v-main>
            <v-container class="pa-2" fluid>
                <v-row>
                    <v-col>
                        <PatientInfo></PatientInfo>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col cols="4">
                        <OriginRecords :annotations="infos" :records="records" :annotations_type="annotations_type">
                        </OriginRecords>
                    </v-col>
                    <v-col cols="8">
                        <v-sheet elevation="5" rounded class="py-3 px-5" min-height="70vh">
                            <h2 class="mb-3">重点信息</h2>
                            <v-sheet class="border rounded-xl pa-3" min-height="100">
                                <InfoTree :config="config" :nodes_obj="nodes_obj" :nodes_array="nodes_array"></InfoTree>
                            </v-sheet>
                        </v-sheet>
                    </v-col>
                </v-row>

            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */
import NavDrawer from '@/apps/CaseBase/CaseDetails/NavDrawer.vue';
import PatientInfo from '@/apps/CaseBase/CaseDetails/CaseView/PatientInfo/PatientInfo.vue';
import OriginRecords from '@/apps/CaseBase/CaseDetails/CaseView/OrginRecords/OriginRecords.vue';
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import InfoTree from './InfoTree.vue';

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');
const route = useRoute();
const backPage = 'Case_Details_View';
const backPage_params = { id: route.params.id };
const annotations_type = 'Info'

const records = ref([
    {
        id: 1,
        text: '患者，男性，藏族，76岁，入院前16年余无明显诱因出现便后出血，约1d后可自行停止，未予重视。入院前8年开始出现磕碰处瘀斑，未予治疗。病程中间断便血，持续时间逐渐延长，便血次数逐渐增多，未系统诊治。入院前 1 年上述症状加重。',
        tags: ['时间段', '患者信息', '症状', '既往史', '个人史'],
        more_tags: ['检查', '血常规'],
    },
    {
        id: 2,
        text: '体格检查：神志清楚，体格检查合作，全身皮肤未见瘀点、瘀斑及皮下出血点，可见散在陈旧性皮疹，双下肢色素沉着，皮肤、巩膜无黄染，全身浅表淋巴结未触及肿大。胸骨无压痛。双肺呼吸音清，未闻及干湿性啰音，律齐，各瓣膜未闻及病理性杂音。全腹软，无压痛及反跳痛。肝脾肋下未触及。双下肢无水肿。',
        tags: ['体格检查', '阳性体征', '阴性体征', '神志', '皮肤'],
        more_tags: ['瘀斑', '皮下出血', '皮疹', '色素沉着', '巩膜', '浅表淋巴结', '胸骨', '肺', '呼吸', '干湿性啰音', '心律', '瓣膜', '病理性杂音', '腹部', '压痛', '反跳痛', '肝脏', '脾脏', '肋骨', '下肢', '水肿']
    },
    {
        id: 3,
        text: '诊断方法： 运用 HE染色、免疫组化、流式免疫分型、染色体核型分析、分子生物学（实时荧光定量 PCR+二代测序）进行诊断及鉴别诊断并分析讨论，血液病理综合诊断为：1.骨髓增生异常肿瘤/急性髓系白血病；2.具有胚系易感性的髓系肿瘤（DDX41 基因突变），无预先存在的血小板疾病或器官功能障碍。',
        tags: ['诊断方法', '诊断结果', '苏木精-伊红染色组织切片', '免疫组织化学方法', '流式细胞术免疫分型'],
        more_tags: ['染色体核型分析', '实时荧光定量pcr', '二代测序', '肿瘤性骨髓增生异常', '急性髓系白血病', '髓系肿瘤', '血小板疾病', '器官功能障碍']
    },
    {
        id: 4,
        text: '诊断：血常规：Hb 107 g/L，RBC 2.93×1012/L，MCV 106.7 fl，WBC 1.94×109/L，Gran% 34.2%，Lym% 60.6%，Mon% 1.5%，PLT 44×109/L。综合 C-MICM 诊断：MDS/AML 伴 ASXL1、SRSF2、TP53、DDX41（双位点）一级突变，提示预后不良，DDX41 的 exon6 c.484del 为胚系突变，具有一定遗传易感性。2022 年国际共识分类（ICC）根据对血液系统恶性肿瘤生物学的最新进展将髓系肿瘤重新分类，其中原始细胞为 10%~19%的骨髓增生异常肿瘤（MDS）被归类为 MDS/急性髓系白血病（AML）',
        tags: ['诊断结果', '疾病分类', 'micm分析', '骨髓增生异常性白血病', '急性髓性白血病'],
        more_tags: ['信号转导和转录激活因子1 ', 'SRSF2', '...']
    },
    {
        id: 5,
        text: '鉴别诊断：MDS/AML 需要鉴别的是 MDS 和AML，据骨髓涂片及流式免疫分型原始细胞计数均小于 20%，不足以诊断 AML，骨髓活检原始细胞可能已超过 20%，可以诊断 AML，但患者起病缓慢，且有皮肤瘀斑病史 8 年，诊断 MDS/AML 更为合适。原始细胞计数为10%~19%的 MDS 病例现在被诊断为 MDS/AML，这反映了 AML 和 MDS 之间的诊断连续性以及原始细胞计数较低的个体患者的临床和遗传异质性',
        tags: ['检查值', '诊断理由', '诊断结果', '知识关系'],
        more_tags: []
    },
    {
        id: 6,
        text: '治疗方法：2023 年6 月 16 日予阿扎胞苷 100 mg d1~7方案行第 1 周期化疗，辅以护胃、升细胞、改善贫血等支持治疗，化疗过程顺利。病程中患者诉全身散在红色皮疹及皮下结节伴瘙痒不适，考虑斯威特综合征可能性大，予甲泼尼龙抗炎，复方氟米松软膏对症止痒，病情好转后出院。',
        tags: ['治疗', '治疗方案', '治疗结果', '症状', '时间点'],
        more_tags: ['出院', '...']
    },
    {
        id: 7,
        text: '临床转归：患者自化疗后，症状及血常规明显改善，精神可，饮食、睡眠可，大小便正常，体重未见明显增减。',
        tags: ['随访', '时间段', ''],
        more_tags: []
    }
]);
// infos由后端组装。重点信息用模板做NER后再做onto锁定，锁不到的取原文
const infos = ref([
    {
        id: 1,
        record_id: 1,
        start: 3,
        end: 12,
        depth: 0,
        ontology: {
            id: 1,
            title: '基本信息',
            value: null,
        },
        children: [11, 12, 13],
    },
    {
        id: 11,
        record_id: 1,
        start: 3,
        end: 5,
        depth: 1,
        ontology: {
            id: 2,
            title: '性别',
            value: {
                id: 21,
                title: '男性',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 12,
        record_id: 1,
        start: 6,
        end: 8,
        depth: 1,
        ontology: {
            id: 3,
            title: '民族',
            value: {
                id: 121,
                title: '藏族',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 13,
        record_id: 1,
        start: 9,
        end: 12,
        depth: 1,
        ontology: {
            id: 4,
            title: '年龄',
            value: 76,
        },
        children: [131],
    },
    {
        id: 131,
        record_id: 1,
        start: 11,
        end: 12,
        depth: 2,
        ontology: {
            id: 41,
            title: '年龄单位',
            value: {
                id: 1311,
                title: '年',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 2,
        record_id: 1,
        start: 13,
        end: 113,
        depth: 0,
        ontology: {
            id: 5,
            title: '既往史',
            value: null,
        },
        children: [22, 23, 24, 25],
    },
    {
        id: 22,
        record_id: 1,
        start: 13,
        end: 47,
        depth: 1,
        ontology: {
            id: 5,
            title: '症状',
            value: {
                id: 221,
                title: '便血',
                value: null,
            },
        },
        children: [221],
    },
    {
        id: 221,
        record_id: 1,
        start: 13,
        end: 16,
        depth: 2,
        ontology: {
            id: 2211,
            title: '时间点',
            value: '入院前',
        },
        children: [222],
    },
    {
        id: 222,
        record_id: 1,
        start: 16,
        end: 20,
        depth: 2,
        ontology: {
            id: 5,
            title: '持续时间',
            value: 16,
        },
        children: [2221, 2222],
    },
    {
        id: 2221,
        record_id: 1,
        start: 18,
        end: 19,
        depth: 3,
        ontology: {
            id: 5,
            title: '时间单位',
            value: {
                id: 1311,
                title: '年',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 2222,
        record_id: 1,
        start: 19,
        end: 20,
        depth: 3,
        ontology: {
            id: 5,
            title: '补充信息',
            value: '余',
        },
        children: [],
    },
    {
        id: 23,
        record_id: 1,
        start: 47,
        end: 67,
        depth: 1,
        ontology: {
            id: 5,
            title: '症状',
            value: {
                id: 231,
                title: '瘀斑',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 24,
        record_id: 1,
        start: 67,
        end: 99,
        depth: 1,
        ontology: {
            id: 5,
            title: '症状',
            value: {
                id: 221,
                title: '便血',
                value: null,
            },
        },
        children: [],
    },
    {
        id: 25,
        record_id: 1,
        start: 99,
        end: 114,
        depth: 1,
        ontology: {
            id: 5,
            title: '补充信息',
            value: '入院前 1 年上述症状加重',
        },
        children: [],
    },
]);
const getNodeText = (info) => {
    const onto = info.ontology;
    if (onto) {
        const onto_value = onto.value;
        if (onto_value) {
            if (typeof (onto_value) === 'object') return onto.title + '：' + onto_value.title;
            else return onto.title + '：' + onto_value;
        }
        else return onto.title;
        // + "：" + records.value.find((record) => {
        //     return record.id == info.record_id
        // }).text.substring(info.start, info.end);
    }
    else return 'Error: NOT FOUND ONTOLOGY'
};
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