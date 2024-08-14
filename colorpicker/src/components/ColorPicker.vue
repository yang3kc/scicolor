<script setup>
import { ref, onMounted } from "vue";
import ColorScheme from "./ColorScheme.vue";
import ColorSwatch from "./ColorSwatch.vue";
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
  <div class="container flex justify-center">
    <ColorSwatch />
  </div>
  <div class="container flex justify-center">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-4">
      <template v-for="color_collection in colors">
        <ColorScheme v-for="(color_scheme, index_scheme) in color_collection.color_schemes" :color_scheme="color_scheme" :key="index_scheme" :color_collection_source="color_collection.collection_source"/>
      </template>
    </div>
  </div>
  </div>
</template>