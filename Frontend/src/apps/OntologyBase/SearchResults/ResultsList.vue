<template>
    <v-container>
        <v-hover v-for="index in 5" :key="index">
            <template v-slot:default="{ isHovering, props }">
                <v-card v-bind="props" :color="isHovering ? 'primary' : undefined" class="mb-5"
                    @click="navToDetails(index)">
                    <v-list-item lines="two" :title="`本体 ${index}`" rounded>
                        <v-list-item-subtitle class="text-truncat">
                            既往史又称过去病史，即就医时医生向患者问询的患者既往的健康状况和过去曾经患过的疾病等方面的问题。
既往健康状况包括饮食习惯等。病人平时健康状况，可能与其现患疾病有一定的关系，故对分析判断现发疾病的病情具有重要的参考价值。
既往患病情况包括包括外科手术史、预防注射史、过敏史及系统回顾等。病人既往所患某些疾病，可能与现患病证有着密切关系。如哮病、痫病、中风等病，经治疗之后，症状虽已消失，但尚未根除，某些诱因常可导致旧病复发。
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-card>
            </template>
        </v-hover>
    </v-container>
</template>

<script setup>
/* Import any necessary modules or components */
import { useRouter } from 'vue-router';
/* Define your component's data using ref */
const router = useRouter();

/* Define your functions */
// const func_a = () => {};
const navToDetails = (id) => {
    router.push({
        name: 'Ontology_Details',
        params: {
            id: id,
        },
    })
};
</script>

<style scoped>
/* Your scoped styles go here */
</style>