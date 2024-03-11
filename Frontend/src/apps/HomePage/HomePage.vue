<!-- src/views/Home.vue -->

<template>
  <v-app id="inspire">
    <NavBar></NavBar>
    <v-main class="bg-grey-lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list rounded="lg">
                <v-list-item v-for="n in 5" :key="n" :title="`案例 ${n}`" link></v-list-item>

                <v-divider class="my-2"></v-divider>

                <v-list-item color="grey-lighten-4" title="Refresh" link></v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet min-height="70vh" rounded="lg">
              <!--  -->
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>

</template>

<script setup>
import NavBar from './NavBar/NavBar.vue';
</script>

<style scoped>
/* You can add component-specific styles here if needed */
</style>
