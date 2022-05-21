<template>
  <div class="container">
    <h1 class="mb-3">Scicolor Color Picker</h1>
    <div class="mb-5">
        <b-form-group class="mb-3">
          <b-form-checkbox-group
            v-model="filterSelected"
            name="flavour-1"
            plain
            @change="filterColorList"
          >
            <b-form-checkbox value="color_blind_friendly" inline>Color blind friendly</b-form-checkbox>
            <b-form-checkbox value="categorical" inline>Categorical</b-form-checkbox>
            <b-form-checkbox value="discrete">Discrete</b-form-checkbox>
            <b-form-checkbox value="diverging">Diverging</b-form-checkbox>
            <b-form-checkbox value="sequential">Sequential</b-form-checkbox>
          </b-form-checkbox-group>
      </b-form-group>
      <b-button @click="restoreColorList()" class="mx-1" variant="outline-dark">Restore</b-button>
      <b-button @click="shuffleColorList()" class="mx-1" variant="outline-secondary">Shuffle</b-button>
    </div>
    <div>
      <b-row v-for="(row, row_index) in colorsToShowChunks" :key="row_index">
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
      colorsJson: colorsJson,
      colorList: colorsJson.slice(),
      filterSelected: []
    }
  },
  computed: {
    colorsToShowChunks: function () {
      // console.log(this.sliceIntoChunks(this.colorsJson, 3));
      return this.sliceIntoChunks(this.colorList, 3);
    },
  },
  methods: {
    sliceIntoChunks: function (arr, chunkSize) {
      const res = [];
      for (let i = 0; i < arr.length; i += chunkSize) {
          const chunk = arr.slice(i, i + chunkSize);
          res.push(chunk);
      }
      return res;
    },
    isSuperset: function (set, subset) {
      for (let elem of subset) {
        if (!set.has(elem)) {
          return false;
        }
      }
      return true;
    },
    restoreColorList: function () {
      this.colorList = this.colorsJson.slice();
      this.filterSelected = [];
    },
    shuffleColorList: function () {
      this.colorList = this.colorList.sort(() => Math.random() - 0.5);
    },
    filterColorList: function () {
      console.log(this.filterSelected);
      var filterSet = new Set(this.filterSelected);
      var newColorList = [];
      for(let color of this.colorsJson){
        var colorLabels = new Set(color["labels"]);
        if(this.isSuperset(colorLabels, filterSet)){
          newColorList.push(color);
        }
      }
      this.colorList = newColorList;
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
