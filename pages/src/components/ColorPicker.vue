<template>
  <div class="container">
    <h1 class="mb-3" v-b-toggle.sidebar>
      Scicolor Color Picker
      <b-icon icon="info-circle" class="h4 ml-2" variant="secondary"></b-icon>
    </h1>
    <div class="mb-3">
        <b-form-group class="mb-3">
          <b-form-checkbox-group
            v-model="filterSelected"
            name="flavour-1"
            plain
            @change="filterColorList"
          >
            <b-form-checkbox value="color_blind_friendly" inline>Color-blind-friendly</b-form-checkbox>
            <b-form-checkbox value="categorical" inline>Categorical</b-form-checkbox>
            <b-form-checkbox value="discrete">Discrete</b-form-checkbox>
            <b-form-checkbox value="diverging">Diverging</b-form-checkbox>
            <b-form-checkbox value="sequential">Sequential</b-form-checkbox>
          </b-form-checkbox-group>
      </b-form-group>
      <b-button @click="shuffleColorList()" class="mx-1" variant="outline-secondary">Shuffle</b-button>
      <b-button @click="restoreColorList()" class="mx-1" variant="outline-dark">Restore</b-button>
    </div>
    <div>
      <b-sidebar id="sidebar" width="500px" title="" shadow right>
        <div class="mx-3 my-3">
        <h3>Tips</h3>
        <p>
          Click the color block to copy the color code.
          Click the "Shuffle" button to shuffle the color list.
          Click the "Restore" button to restore to the default view.
          Use the check boxes to filter the colors.
        </p>
        <h3>About</h3>
        <p>
          This is <a href="https://www.kaichengyang.me" target="_blank"> Kevin</a>'s collection of colors for scientific visualizations.
          Currently, only discrete and categorical colors are included.
          For continuous schemes, check out the Python package <a href="https://pypi.org/project/scicolor/"><code>scicolor</code></a>.
        </p>
        <p>
          Colors listed come form
          <a href="https://help.tableau.com/current/pro/desktop/en-us/formatting_create_custom_colors.htm" target="_blank">Tableau</a>,
          <a href="https://github.com/karthik/wesanderson" target="_blank">Wes Anderson Palettes</a>,
          and <a href="https://github.com/BlakeRMills/MetBrewer" target="_blank">MetBrewer</a>.
        </p>
        <p>
          <a href="https://github.com/yangkcatiu/scicolor" target="_blank">
            <b-icon icon="github" class="h1 ml-2" variant="secondary"></b-icon>
          </a>
        </p>
        </div>
      </b-sidebar>
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
