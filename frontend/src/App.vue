<template>
  <SensorChart msg="Welcome to Your Vue.js + TypeScript App" />
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import SensorChart from "./components/SensorChart.vue";

@Options({
  components: {
    SensorChart,
  },
})
export default class App extends Vue {}
</script>

<style></style>
