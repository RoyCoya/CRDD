<template>
  <div>
    <h1>Data from Backend</h1>
    <p>calling: {{ url }}</p>
    <ul>
      <li v-for="item in data" :key="item.id">{{ item.comments }}</li>
    </ul>
  </div>
</template>
  
<script>
import backend from "@/configs/backend";
import axios from 'axios';

const url = backend.backendBaseUrl + backend.mainFrameBaseUrl + 'test'
console.log(url)

export default {
  data() {
    return {
      url : url,
      data: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    loadData() {
      // 发起 API 请求
      axios.get(url)
        .then(response => {
          // 处理响应数据
          this.data = response.data;
        })
        .catch(error => {
          // 处理错误
          console.error(error);
        });
    }
  }
}
</script>
  