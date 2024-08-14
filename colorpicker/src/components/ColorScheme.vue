<script setup>
import { ref } from 'vue';

const props = defineProps({
    color_collection_source: {
        type: Object,
        required: true
    },
    color_scheme: {
        type: Object,
        required: true
    }
});

const showToast = ref(false);
const toastMessage = ref('');
const toastMessageColor = ref('');

const copy_color_code = (color) => {
    navigator.clipboard.writeText(color);
    showToast.value = true;
    toastMessage.value = `Color ${color} copied to clipboard!`;
    toastMessageColor.value = color;
    setTimeout(() => {
        showToast.value = false;
    }, 3000);
}
</script>

<template>
  <div>
    <div class="flex gap-0 w-[310px]">
      <div v-for="(color, color_index) in color_scheme.colors"
        :key="color_index"
        class="w-full h-[40px] dropdown dropdown-hover dropdown-bottom"
        :style="{'background-color': color}"
        role="button"
        tabindex="0"
        >
        <div tabindex="0" class="card compact dropdown-content z-[1] bg-base-100 shadow w-[200px]">
          <div class="card-body">
            <p class="prose font-mono font-bold text-center" @click="copy_color_code(color)">{{ color }}</p>
            <div class="h-[40px]" :style="{'background-color': color}" @click="copy_color_code(color)"></div>
            <div class="btn btn-sm btn-ghost" @click="copy_color_code(color)">Copy color code</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <p class="prose mt-1"><a class="link" :href="color_collection_source.url">{{ color_collection_source.name }}</a> - {{ color_scheme.name }}</p>
    </div>
    <!-- toast  -->
    <div v-if="showToast" class="toast">
      <div class="alert" :style="{'background-color': toastMessageColor}">
        <div class="flex-1">
          <span class="text-white">{{ toastMessage }}</span>
        </div>
      </div>
    </div>
  </div>
</template>