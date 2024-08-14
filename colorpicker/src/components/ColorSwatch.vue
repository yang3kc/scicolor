<script setup>
import { ref } from 'vue';
import Toast from '@/components/Toast.vue';
import { color_swatch_store } from '@/components/ColorSwatchStore.js';
// data
const toast_func = ref(null);

// methods
const copy_color_code = (color) => {
    navigator.clipboard.writeText(color);
    toast_func.value.showToast(`Color ${color} copied to clipboard!`, color);
}

const copy_all_color_codes = () => {
    const color_codes = JSON.stringify(color_swatch_store.colors, null, 2);
    navigator.clipboard.writeText(color_codes);
    toast_func.value.showToast(`All color codes copied to clipboard!`, "#1f77b4");
}

</script>

<template>
  <div v-if="color_swatch_store.colors.length > 0">
    <div class="flex gap-0 w-[310px] md:w-[800px]">
      <div v-for="(color, color_index) in color_swatch_store.colors"
        :key="color_index"
        class="w-full h-[40px] dropdown dropdown-hover dropdown-bottom"
        :style="{'background-color': color}"
        role="button"
        tabindex="0"
        >
        <div tabindex="0" class="card compact dropdown-content z-[1] bg-base-100 shadow w-[200px]">
          <div class="card-body">
            <div class="h-[36px]" :style="{'background-color': color}" @click="copy_color_code(color)">
              <p class="prose font-mono font-bold text-center mt-1" @click="copy_color_code(color)">{{ color }}</p>
            </div>
            <div class="btn btn-sm btn-ghost" @click="copy_color_code(color)">
              <font-awesome-icon :icon="['far', 'copy']" />
              Copy color code</div>
            <div class="btn btn-sm btn-ghost" @click="color_swatch_store.remove_color(color_index)">
              <font-awesome-icon :icon="['far', 'trash-can']" />
              Remove color</div>
            <div class="btn btn-sm btn-ghost" @click="color_swatch_store.move_color_left(color_index)">
              <font-awesome-icon :icon="['far', 'circle-left']" />
              Move left</div>
            <div class="btn btn-sm btn-ghost" @click="color_swatch_store.move_color_right(color_index)">
              <font-awesome-icon :icon="['far', 'circle-right']" />
              Move right</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex max-md:flex-col md:justify-center items-center">
      <div role="button" class="btn btn-sm btn-outline btn-ghost mr-2 mt-2" @click="color_swatch_store.remove_all_colors()">
        <font-awesome-icon :icon="['far', 'trash-can']" />
        Remove all colors</div>
      <div role="button" class="btn btn-sm btn-outline btn-ghost mt-2" @click="copy_all_color_codes">
        <font-awesome-icon :icon="['far', 'copy']" />
        Copy all color codes</div>
    </div>
    <Toast ref="toast_func"/>
  </div>
</template>