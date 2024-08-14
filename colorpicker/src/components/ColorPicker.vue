<script setup>
import { ref, onMounted } from "vue";

const colors = ref({});

onMounted(() => {
  fetch("/scicolor/colors/colors.json")
    .then((response) => response.json())
    .then((data) => {
      colors.value = data;
      console.log(colors.value);
    });
});

const hello = ref("Hello World");
</script>

<template>
  <div class="container">
    <h1>{{ hello }}</h1>
  </div>
</template>