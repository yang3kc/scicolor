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
    <p>{{ colorData.collection }} - {{ colorData.name }}</p>
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
    },
  },
  computed: {
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