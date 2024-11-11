<template>
    <div>
        本页面为测试页面
    </div>
    <v-btn @click="fetchData">测试按钮</v-btn>
</template>

<script setup>
/* Import */
import { ref } from 'vue';
import apiClient from '@/configs/api/auth';

const test = () => {
    alert(1)
}

const fetchData = async () => {
    try {
        const response = await apiClient.post('/test/');
        console.log(response.data);
        
        return response;
    } catch (error) {
        console.error("获取数据出错", error);
    }
};
/* Data */

/* Functions */

/* Define things you need to do on mounted */

</script>

<style scoped>
/* Your scoped styles go here */
</style>