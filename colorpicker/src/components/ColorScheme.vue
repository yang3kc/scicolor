<script setup>
import { ref } from 'vue';
import Toast from '@/components/Toast.vue';
import { color_swatch_store } from '@/components/ColorSwatchStore.js';
import { getTextColor } from '@/components/utils.js';

// props
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

// data
const toast_func = ref(null);

// methods
const copy_color_code = (color) => {
    navigator.clipboard.writeText(color);
    toast_func.value.showToast(`Color ${color} copied to clipboard!`, color);
}

const copy_color_codes = (color_codes) => {
    const color_codes_string = JSON.stringify(color_codes, null, 2);
    navigator.clipboard.writeText(color_codes_string  );
    toast_func.value.showToast(`All color codes copied to clipboard!`, "#1f77b4");
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
        <div tabindex="0" class="card compact dropdown-content z-[1] bg-base-100 shadow w-[230px]">
          <div class="card-body">
            <div class="h-[36px] rounded-lg" :style="{'background-color': color}" @click="copy_color_code(color)">
              <p class="prose font-mono font-bold text-center mt-1" :style="{'color': getTextColor(color)}" @click="copy_color_code(color)">{{ color }}</p>
            </div>
            <div class="btn btn-sm btn-outline" @click="copy_color_code(color)">
              <font-awesome-icon :icon="['far', 'copy']" />
              Copy color code</div>
            <div class="btn btn-sm btn-outline" @click="color_swatch_store.add_color(color)">
              <font-awesome-icon :icon="['far', 'square-plus']" />
              Add to color swatch</div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <p class="prose mt-1"><a class="link" :href="color_collection_source.url" target="_blank">{{ color_collection_source.name }}</a> - {{ color_scheme.name }} <font-awesome-icon :icon="['far', 'copy']" @click="copy_color_codes(color_scheme.colors)" class="hover:text-primary hover:text-lg" /></p>
    </div>
    <Toast ref="toast_func"/>
  </div>
</template>