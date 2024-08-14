<script setup>
import { ref, onMounted } from "vue";
import ColorScheme from "./ColorScheme.vue";
import ColorSwatch from "./ColorSwatch.vue";
import { color_swatch_store } from "./ColorSwatchStore.js";
const colors = ref({});

onMounted(() => {
  fetch("/scicolor/colors/colors.json")
    .then((response) => response.json())
    .then((data) => {
      colors.value = data;
      console.log(colors.value);
    });
});
</script>

<template>
  <div>
  <template v-if="color_swatch_store.colors.length > 0">
    <hr class="my-4">
    <h2 class="text-2xl font-bold text-center mb-4">Color Swatches 🎨</h2>
    <div class="container flex justify-center mb-4">
      <ColorSwatch />
    </div>
  </template>
  <hr class="my-4">
  <h2 class="text-2xl font-bold text-center mb-4">Color Collections 🌈</h2>
  <div class="container flex justify-center">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-4">
      <template v-for="color_collection in colors">
        <ColorScheme v-for="(color_scheme, index_scheme) in color_collection.color_schemes" :color_scheme="color_scheme" :key="index_scheme" :color_collection_source="color_collection.collection_source"/>
      </template>
    </div>
  </div>
  </div>
</template>