<template>
    <v-container>
        <v-row>
            <v-col><v-combobox v-model="query" no-data-text="未找到相关内容" class="pa-3" density="compact" placeholder=""
                    prepend-inner-icon="mdi-magnify" theme="light" variant="solo" item-props
                    rounded></v-combobox></v-col>
        </v-row>
        <v-row>
            <v-col class="px-5">
                <h2>相关医学概念</h2>
                <ol>
                    <li>
                        <a href="#">便血</a>
                        <ul>
                            <li>便血是指粪便中混有血液，表现为鲜红色、暗红色或黑色，取决于出血的部位和量。</li>
                            <li>常见的原因包括痔疮、肛裂、结肠癌、消化性溃疡、克罗恩病和溃疡性结肠炎等。</li>
                            <li>诊断依据包括粪便隐血试验、肛门指检、肠镜检查、血液学检查（如血常规和凝血功能检查）及影像学检查（如CT和MRI）。</li>
                        </ul>
                    </li>

                    <br>
                    <li>
                        <a href="#">骨髓增生异常肿瘤</a>
                        <ul>
                            <li>该疾病是指骨髓内干细胞或造血干细胞发生异常克隆增生，导致血细胞的异常增殖和成熟障碍。</li>
                            <li>通常表现为贫血、出血倾向和感染易发等临床表现。</li>
                            <li>诊断依据包括骨髓活检、血液学检查（如血常规和骨髓细胞学检查）及分子生物学检测。</li>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <a href="#">急性髓系白血病</a>
                        <ul>
                            <li>急性髓系白血病是一种由于骨髓内克隆性干细胞异常增殖而导致的血液系统恶性肿瘤。</li>
                            <li>临床表现包括突发的贫血、出血倾向、发热及感染。</li>
                            <li>诊断需要通过骨髓象形学检查及分子遗传学检测。</li>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <a href="#">MDS/AML</a>
                        <ul>
                            <li>MDS/AML是骨髓增生异常肿瘤和急性髓系白血病的混合病理类型，通常表现为骨髓增生异常伴有白血病的克隆性进展。</li>
                            <li>诊断依据包括血液学特征、骨髓象形学及分子遗传学分析。</li>
                            <li>治疗策略包括化疗及支持治疗，预后取决于病情的严重程度及分子遗传学特征。</li>
                        </ul>
                    </li>
                    <br>
                    <li>
                        <a href="#">DDX41基因突变</a>
                        <ul>
                            <li>DDX41基因突变是一种稀有的骨髓增生异常相关基因突变，可能导致造血干细胞的克隆性增殖。</li>
                            <li>常见于特定的家族性或遗传易感群体中，与部分骨髓增生异常肿瘤及急性髓系白血病有关。</li>
                        </ul>
                    </li>
                </ol>

            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { ref } from 'vue';

/* Import */

/* Data */
const query = ref(null)
/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>