<template>
  <div class="container">
    <h1>Color Picker</h1>
    <div>
      <b-row v-for="(row, row_index) in colors_to_show" :key="row_index">
        <b-col v-for="(col, col_index)  in row" :key="col_index">
          <ColorUnit v-bind:colorData="col"/>
        </b-col>
      </b-row>
    </div>

  </div>
</template>

<script>
import ColorUnit from './ColorUnit'
import colorsJson from './colors.json'

export default {
  name: 'ColorPicker',
  components: {
    ColorUnit
  },
  data () {
    return {
      colorsJson: colorsJson
    }
  },
  computed: {
    colors_to_show: function () {
      // console.log(this.sliceIntoChunks(this.colorsJson, 3));
      return this.sliceIntoChunks(this.colorsJson, 3);
    }
  },
  methods: {
    sliceIntoChunks: function (arr, chunkSize) {
      const res = [];
      for (let i = 0; i < arr.length; i += chunkSize) {
          const chunk = arr.slice(i, i + chunkSize);
          res.push(chunk);
      }
      return res;
    }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
span {
  display: inline-block;
  position: relative;
  height: 40px;
}
</style>
