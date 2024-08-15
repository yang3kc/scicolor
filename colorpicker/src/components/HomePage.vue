<script setup>
import ColorPicker from "@/components/ColorPicker.vue";
</script>

<template>
  <div class="drawer container mx-auto max-w-screen-xl p-4">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <label for="my-drawer" class="drawer-button flex justify-center">
        <!-- Page content -->
        <h1 class="text-2xl font-medium text-center prose">Scicolor Color Picker</h1>
        <font-awesome-icon :icon="['far', 'circle-question']" class="ml-2"/>
      </label>
      <ColorPicker />
    </div>
    <div class="drawer-side">
      <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
      <div class="bg-base-200 min-h-full w-60 md:w-80 p-4 text-center">
        <!-- Sidebar content here -->
        <p class="prose text-xl font-medium">Instructions</p>
        <p class="prose leading-5">
          Hover over or click on a color to see its hex code, copy the code to your clipboard directly, or add it to the Color Swatches for screening.
          Click <font-awesome-icon :icon="['far', 'copy']" /> to copy the whole color palette.
        </p>
        <p class="prose text-xl font-medium mt-4">About</p>
        <p class="prose leading-5">
          This is <a class="link" href="https://www.kaichengyang.me" target="_blank"> Kevin</a>'s collection of colors for scientific visualizations.
          Currently, only discrete and categorical color schemes are included.
          For continuous schemes, check out the Python package <a class="link" href="https://pypi.org/project/scicolor/"><code>scicolor</code></a>.
        </p>
        <p class="prose leading-5 mt-2">
          The color palettes are collected from different sources linked in each color palette.
        </p>
        <p class="prose leading-5 mt-2">
          This tool is implemented as a <a class="link" href="https://vuejs.org/">Vue.js</a> app, with <a class="link" href="https://tailwindcss.com/">Tailwind CSS</a> and <a class="link" href="https://daisyui.com/">daisyUI</a> for styling.
          The icons are from <a class="link" href="https://fontawesome.com/">Font Awesome</a>.
        </p>
        <div class="flex justify-center mt-4">
          <a href="https://twitter.com/yang3kc" target="_blank">
            <font-awesome-icon :icon="['fab', 'twitter']" class="text-2xl mr-2 text-gray-700"/>
          </a>
          <a href="https://github.com/yang3kc/scicolor" target="_blank">
            <font-awesome-icon :icon="['fab', 'github']" class="text-2xl text-gray-700"/>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
