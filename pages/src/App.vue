<template>
  <div id="app">
    <ColorPicker/>
  </div>
</template>

<script>
import ColorPicker from './components/ColorPicker.vue'

export default {
  name: 'App',
  components: {
    ColorPicker
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
