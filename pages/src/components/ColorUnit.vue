<template>
<div>
  <div>
    <span
    v-for="(color, color_index) in colorData.colors"
    :key="color_index"
    v-bind:style="{ 'background-color': color, width: colorWidth }"
    v-b-tooltip.hover.v-secondary :title="color"
    @click="copy(color)"
    ></span>
  </div>
  <div>
    <p>
      {{ colorData.collection }} - {{ colorData.name }}
      <b-icon
      icon="files"
      class="ml-5"
      @click="copy(colorList)"
       v-b-tooltip.hover.v-secondary :title="colorList"
      ></b-icon>
    </p>
  </div>
</div>
</template>

<script>
export default {
  name: 'ColorUnit',
  props: {
    colorData: {
      type: Object,
      default: Object
    },
    totalWidth: {
      type: Number,
      default: 360
    }
  },
  methods: {
    async copy(s) {
      await navigator.clipboard.writeText(s);
    }
  },
  computed: {
    colorList: function () {
      return JSON.stringify(this.colorData.colors, null, " ");
    },
    colorWidth: function () {
      return (this.totalWidth / this.colorData.colors.length).toString() + "px";
    }
  }
}
</script>

<style scoped>
span {
  display: inline-block;
  position: relative;
  height: 40px;
}
</style>