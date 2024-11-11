<template>
    <v-app>
        <NavBar></NavBar>
        <v-main>
            <v-container>
                <v-row style="margin-top:10vh">
                    <v-col cols="3"></v-col>
                    <v-col cols="6" class="border-lg elevation-5 pa-10">
                        <v-tabs v-model="activeTab" background-color="primary" dark>
                            <v-tab value="login">登录</v-tab>
                            <v-tab value="registration" disabled>注册</v-tab>
                        </v-tabs>
                        <v-tabs-window v-model="activeTab" width="100%">
                            <v-tabs-window-item value="login">
                                <v-card>
                                    <v-card-title>登录到您的账户</v-card-title>
                                    <v-card-text>
                                        <v-form ref="loginForm">
                                            <v-text-field label="用户名" v-model="loginData.username"
                                                prepend-icon="mdi-account" :rules="[v => !!v || '用户名是必填项']"
                                                required></v-text-field>

                                            <v-text-field label="密码" v-model="loginData.password" type="password"
                                                prepend-icon="mdi-lock" :rules="[v => !!v || '密码是必填项']"
                                                required></v-text-field>

                                            <v-btn color="primary" block class="mt-4" @click="loginUser">
                                                登录
                                            </v-btn>
                                        </v-form>
                                    </v-card-text>
                                </v-card>
                            </v-tabs-window-item>
                            <v-tabs-window-item value="registration">
                                <v-card>
                                    <v-card-title>创建新账户</v-card-title>
                                    <v-card-text>
                                        <v-form>
                                            <v-text-field label="用户名" v-model="registerData.username"
                                                prepend-icon="mdi-account"></v-text-field>
                                            <v-text-field label="密码" v-model="registerData.password" type="password"
                                                prepend-icon="mdi-lock"></v-text-field>
                                            <v-text-field label="确认密码" v-model="registerData.confirmPassword"
                                                type="password" prepend-icon="mdi-lock"></v-text-field>
                                            <v-btn color="primary" block class="mt-4" @click="register">
                                                注册
                                            </v-btn>
                                        </v-form>
                                    </v-card-text>
                                </v-card>
                            </v-tabs-window-item>
                        </v-tabs-window>
                    </v-col>
                    <v-col cols="3"></v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
import { ref } from 'vue';
import NavBar from '@/apps/HomePage/NavBar/NavBar.vue';
import { login } from '@/apps/HomePage/UserAuthorization/authorization';
import { useRouter } from 'vue-router';

/* Data */
const router = useRouter()
const activeTab = ref(0); // 0 = 登录, 1 = 注册
const loginForm = ref(null);
const loginData = ref({
    username: '',
    password: ''
});

const loginUser = async () => {
    const isValid = await loginForm.value.validate();
    if (!isValid) {
        console.log("表单验证未通过");
        return;
    }
    loginRequest();
};

const loginRequest = async() => {
    try {
        const response = await login(loginData.value.username, loginData.value.password);
        switch (response.status) {
            case 200:
                {
                    const { access, refresh } = response.data; // 获取 tokens
                    localStorage.setItem('accessToken', access);
                    localStorage.setItem('refreshToken', refresh);
                    alert('登录成功！');
                    const redirect = router.currentRoute?.value?.query?.redirect || '/'
                    router.push(redirect || '/');
                    break;
                }
            case 401:
                alert('账户密码错误，登录失败！');
                break;
            default:
                break;
        }
    } catch (error) {
        console.error('登录出错：', error);
        alert('登录时出现问题，请联系管理员检查服务器');
    }
}

const registerData = ref({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
});

/* Functions */
// const login = () => {
//     // 登录逻辑
// };
// const register = () => {
//     // 注册逻辑
// };
</script>

<style scoped></style>