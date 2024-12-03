<template>
    <v-app>
        <v-main>
            <v-container>
                <router-link to="/">
                    <<< 返回 </router-link>
                        <v-row>
                            <v-col cols="6">
                                <v-file-input clearable label="上传临床记录" variant="outlined"></v-file-input>
                            </v-col>
                            <v-col cols="4">
                                <v-btn variant="outlined" @click="handleUpload">
                                    上传
                                </v-btn>
                                <span v-if="uploading" class="ms-3">
                                    <v-progress-circular indeterminate color="primary"></v-progress-circular>
                                </span>
                            </v-col>
                        </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>

<script setup>
/* Import any necessary modules or components */

/* Define your component's data using ref */
// const myData = ref('Hello, Vue 3!');

/* Define your functions */
// const func_a = () => {};
import { useRouter } from 'vue-router';
import {ref} from 'vue';

const router = useRouter();
const uploading = ref(false);

const handleUpload = () => {
    // Add any upload logic here, if needed
    setTimeout(() => {
        router.push('/case/details/1');
    }, 3000); // 3-second delay
    uploading.value = true;
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>