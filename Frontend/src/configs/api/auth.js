// src/api/apiClient.js
import axios from 'axios';
import { useRouter } from 'vue-router';
import backend from './backend';

const router = useRouter();

const apiClient = axios.create({
    baseURL: backend.backendBaseUrl,
    timeout: 60000,
});

// 请求拦截器
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('accessToken');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

// 响应拦截器
apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 401) {
            localStorage.removeItem('accessToken');
            localStorage.removeItem('refreshToken');
            alert('登录状态已过期，请重新登录。');
            router.push('/login');
        }
        return Promise.reject(error);
    }
);

export default apiClient;