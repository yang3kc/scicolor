<script setup>
import { ref, onMounted, computed } from "vue";
import ColorScheme from "./ColorScheme.vue";
import ColorSwatch from "./ColorSwatch.vue";
import { color_swatch_store } from "./ColorSwatchStore.js";

// data
const original_color_list = ref([]);
const color_list_template = ref([]);
const only_color_blind_friendly = ref(false);
const at_least_colors = ref(0);

// methods
onMounted(() => {
  fetch("/scicolor/colors/colors.json")
    .then((response) => response.json())
    .then((data) => {
      for (const color_collection of data) {
        for (const color_scheme of color_collection.color_schemes) {
          color_scheme.collection_source = color_collection.collection_source;
          original_color_list.value.push(color_scheme);
        }
      }
      // Create a separate copy of the original_color_list
      color_list_template.value = [...original_color_list.value];
    });
});

const color_list_to_show = computed(() => {
  let temp_color_list = [...color_list_template.value];
  temp_color_list = temp_color_list.filter((color_scheme) => color_scheme.colors.length >= at_least_colors.value);
  if (only_color_blind_friendly.value) {
    temp_color_list = temp_color_list.filter((color_scheme) => color_scheme.labels.includes("color_blind_friendly"));
  }
  return temp_color_list;
});

const shuffle_color_list = () => {
  color_list_template.value = color_list_template.value.sort(() => Math.random() - 0.5);
};

const restore_color_list = () => {
  only_color_blind_friendly.value = false;
  at_least_colors.value = 0;
  color_list_template.value = [...original_color_list.value];
};

</script>

<template>
  <div>
  <template v-if="color_swatch_store.colors.length > 0">
    <hr class="my-4">
    <h2 class="text-2xl font-medium text-center mb-4 prose">Color Swatches 🎨</h2>
    <div class="container flex justify-center mb-4">
      <ColorSwatch />
    </div>
  </template>
  <hr class="my-4">
  <h2 class="text-2xl font-medium text-center mb-2 prose">Color Collections 🌈</h2>
  <!-- controls -->
  <div>
    <div class="flex justify-center">
      <div class="btn btn-sm btn-outline w-25 mr-2" @click="shuffle_color_list">
        <font-awesome-icon :icon="['fas', 'shuffle']" />
        Shuffle
      </div>
      <div class="btn btn-sm btn-outline w-25" @click="restore_color_list">
        <font-awesome-icon :icon="['fas', 'backward-step']" />
        Restore
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 md:max-w-xl mx-auto my-2">
      <div class="form-control">
        <label class="label cursor-pointer flex justify-center md:justify-end">
          <span class="label-text prose mr-2">Only color-blind friendly</span>
          <input type="checkbox" class="toggle toggle-sm" v-model="only_color_blind_friendly" />
        </label>
      </div>
      <div class="form-control flex items-center">
        <label class="label cursor-pointer">
          <span class="label-text prose mr-2">At least {{ at_least_colors }} colors</span>
          <input type="range" min="0" max="15" v-model="at_least_colors" class="range range-xs w-40" />
        </label>
      </div>
    </div>
  </div>
  <div class="container flex justify-center">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-x-8 gap-y-4">
      <template v-for="color_scheme in color_list_to_show" :key="color_scheme.name">
        <ColorScheme :color_scheme="color_scheme" :color_collection_source="color_scheme.collection_source"/>
      </template>
    </div>
</div>
</div>
</template>