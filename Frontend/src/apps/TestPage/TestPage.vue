<template>
    <div>
        本页面为测试页面
    </div>
    <div>
        <span>登录状态：{{ isLoggedIn() }}</span>
    </div>
    <v-btn @click="authTest">用户验证测试</v-btn>
    <v-btn @click="getUserInfo">用户数据获取测试</v-btn>
</template>

<script setup>
/* Import */
import { ref } from 'vue';
import { jwtDecode } from 'jwt-decode';
import apiClient from '@/configs/api/auth';

const authTest = async () => {
    try {
        const response = await apiClient.post('/test/');
        alert("成功。返回数据见调试台")
        console.log(response.data);
        
        return response;
    } catch (error) {
        alert("失败")
        console.error("获取数据出错", error);
    }
};

const isTokenValid = (token) => {
    const decoded = jwtDecode(token);
    const currentTime = Math.floor(Date.now() / 1000); // 当前时间（秒）
    return decoded.exp > currentTime;
}

const isLoggedIn = () => {
    const token = localStorage.getItem('accessToken');
    return token && isTokenValid(token);
}

const getUserInfo = async () => {
    try {
        const response = await apiClient.post('/users/');
        alert("成功。返回数据见调试台")
        console.log(response.data);
        
        return response;
    } catch (error) {
        alert("失败")
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