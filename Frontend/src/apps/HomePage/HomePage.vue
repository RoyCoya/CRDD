<!-- src/views/Home.vue -->

<template>
  <v-app>
    <NavBar></NavBar>
    <v-main class="bg-grey-lighten-3">
      <v-container>
        <v-row>
          <v-col cols="10">
            <v-sheet min-height="80vh" class="pa-10" rounded="lg">
              <v-skeleton-loader type="card"></v-skeleton-loader>
              <v-skeleton-loader type="card"></v-skeleton-loader>
              <v-skeleton-loader type="card"></v-skeleton-loader>
            </v-sheet>
          </v-col>

          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list rounded="lg">
                <v-list-item v-for="n in 5" :key="n" :title="`快捷功能 ${n}`" link></v-list-item>
                <v-divider class="my-2"></v-divider>
                <v-list-item class="text-grey-lighten-1" color="" title="查看全部 >>>" link></v-list-item>
              </v-list>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>

</template>

<script setup>
import NavBar from '@/apps/HomePage/NavBar/NavBar.vue';
</script>

<style scoped>
/* You can add component-specific styles here if needed */
</style>
