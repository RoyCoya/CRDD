<template>
  <div>
    <p>URL: {{ url }}</p>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import backend from "@/configs/api/backend";
import axios from 'axios';

// 定义变量
const url = backend.backendBaseUrl + backend.mainFrameBaseUrl + 'test';
console.log(url);

const data = ref(null);

// 定义方法
const loadData = async () => {
  try {
    const response = await axios.get(url);
    data.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

// 生命周期钩子
onMounted(() => {
  loadData();
});
</script>