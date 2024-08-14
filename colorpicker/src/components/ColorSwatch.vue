<script setup>
import { ref } from 'vue';
import Toast from '@/components/Toast.vue';

// data
const colors = ref([
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]);
const toast_func = ref(null);

// methods
const copy_color_code = (color) => {
    navigator.clipboard.writeText(color);
    toast_func.value.showToast(`Color ${color} copied to clipboard!`, color);
}

</script>

<template>
  <div>
    <div class="flex gap-0 w-[310px]">
      <div v-for="(color, color_index) in colors"
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
    <Toast ref="toast_func"/>
  </div>
</template>