import { reactive } from 'vue';

export const color_swatch_store = reactive({
  colors: [],
  add_color: (color) => {
    color_swatch_store.colors.push(color);
  },
  remove_color: (color_index) => {
    color_swatch_store.colors.splice(color_index, 1);
  },
  move_color_left: (color_index) => {
    if (color_index > 0) {
      const color = color_swatch_store.colors[color_index];
      color_swatch_store.colors.splice(color_index, 1);
      color_swatch_store.colors.splice(color_index - 1, 0, color);
    }
  },
  move_color_right: (color_index) => {
    if (color_index < color_swatch_store.colors.length - 1) {
      const color = color_swatch_store.colors[color_index];
      color_swatch_store.colors.splice(color_index, 1);
      color_swatch_store.colors.splice(color_index + 1, 0, color);
    }
  },
});