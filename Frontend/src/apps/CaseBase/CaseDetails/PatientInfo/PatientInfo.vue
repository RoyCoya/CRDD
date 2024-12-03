<template>
    <v-card elevation="5" class="px-5 pt-3">
        <v-sheet class="text-body-2">
            <v-row align="center">
                <v-col cols="1">姓名：xxx</v-col>
                <v-col cols="1">性别：男</v-col>
                <v-col cols="1">年龄：76</v-col>
                <v-col cols="1">民族：藏族</v-col>
                <v-col cols="8">诊断结果（ICD）：
                    <v-chip 
                        size="small" 
                        variant="elevated" 
                        class="me-1"
                        @click="handleChipClick('http://localhost:5173/ontology/concepts/4:aa1191bf-f20c-428e-9647-29cc6bd62897:34187512')"
                    >
                        <v-tooltip location="bottom" activator="parent" text="D46.900"></v-tooltip>
                        骨髓增生异常肿瘤
                    </v-chip>

                    <v-chip 
                        size="small" 
                        variant="elevated" 
                        class="me-1"
                        @click="handleChipClick('http://localhost:5173/ontology/concepts/4:aa1191bf-f20c-428e-9647-29cc6bd62897:14522470')"
                    >
                        <v-tooltip location="bottom" activator="parent" text="C92.000"></v-tooltip>
                        急性髓系白血病
                    </v-chip>
                </v-col>
            </v-row>
            <v-row align="center">
                <v-col cols="3">现病史：
                    <v-chip 
                        size="small" 
                        variant="elevated" 
                        class="me-1"
                        @click="handleChipClick('http://localhost:5173/ontology/concepts/4:aa1191bf-f20c-428e-9647-29cc6bd62897:30637534')"
                    >
                        <v-tooltip location="bottom" activator="parent" text="K92.1"></v-tooltip>
                        便血
                    </v-chip>
                </v-col>
                <v-col cols="3">既往史：
                    <v-chip 
                        size="small" 
                        variant="elevated" 
                        class="me-1"
                        @click="handleChipClick('http://localhost:5173/ontology/concepts/4:aa1191bf-f20c-428e-9647-29cc6bd62897:30637534')"
                    >
                        <v-tooltip location="bottom" activator="parent" text="K92.1"></v-tooltip>
                        便血
                    </v-chip>
                    <v-chip 
                        size="small" 
                        variant="elevated" 
                        class="me-1"
                        @click="handleChipClick('http://localhost:5173/ontology/concepts/4:aa1191bf-f20c-428e-9647-29cc6bd62897:15437298')"
                    >
                        <v-tooltip location="bottom" activator="parent" text="K92.1"></v-tooltip>
                        淤斑
                    </v-chip>
                </v-col>
                <v-col cols="2">个人史：</v-col>
                <v-col cols="2">家族史：无</v-col>
                <v-col cols="2">过敏史：无</v-col>
            </v-row>
        </v-sheet>
        <v-card-actions class="d-flex justify-end">
            <v-btn variant="tonal" size="small" @click="reveal_patient_info = true" color="grey-darken-1">查看所有
                >>></v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

// 跳转逻辑
const handleChipClick = (link) => {
  // 如果需要跳转到外部页面
  if (link.startsWith('http')) {
    window.open(link, '_blank'); // 打开新标签页
  } else {
    // 如果需要在应用内跳转
    router.push(link);
  }
};

const reveal_patient_info = false;
</script>

<style scoped>
/* Your scoped styles go here */
</style>