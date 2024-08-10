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
            <b-form-select class="mx-4" v-model="collectionSelected" :options="collectionNames" @change="filterColorList"></b-form-select>
            <label for="sb-inline">With at least</label>
            <b-form-spinbutton id="sb-inline" class="mx-2" v-model="colorCnt" size="sm" inline @change="filterColorList"></b-form-spinbutton>
            <label for="sb-inline">colors</label>
      </b-form-group>
      <b-button @click="shuffleColorList()" class="mx-1" variant="outline-secondary">Shuffle</b-button>
      <b-button @click="restoreColorList()" class="mx-1" variant="outline-dark">Restore</b-button>
    </div>
    <div class="mb-3">Click color block to copy the color code. Click <b-icon icon="files"></b-icon> to copy the whole list.</div>
    <div>
      <b-sidebar id="sidebar" width="500px" title="" shadow right>
        <div class="mx-3 my-3">
        <h3>Tips</h3>
        <p class="mb-0">Click color block to copy the color code.</p>
        <p class="mb-0">Click <b-icon icon="files"></b-icon> to copy the whole list.</p>
        <p class="mb-0">Click "Shuffle" button to shuffle the color list.</p>
        <p class="mb-0">Click "Restore" button to restore to the default view.</p>
        <p class="mb-0">Use checkboxes to filter the colors.</p>
        <h3 class="mt-5">About</h3>
        <p>
          This is <a href="https://www.kaichengyang.me" target="_blank"> Kevin</a>'s collection of colors for scientific visualizations.
          Currently, only discrete and categorical color schemes are included.
          For continuous schemes, check out the Python package <a href="https://pypi.org/project/scicolor/"><code>scicolor</code></a>.
        </p>
        <p>
          Colors listed come form
          <a href="https://help.tableau.com/current/pro/desktop/en-us/formatting_create_custom_colors.htm" target="_blank">Tableau</a>,
          <a href="https://www.nordtheme.com" target="_blank">Nord</a>,
          <a href="https://github.com/karthik/wesanderson" target="_blank">Wes Anderson Palettes</a>,
          <a href="https://www.rpthjournal.org/article/S2475-0379(22)01983-5/pdf" target="_blank">RPTH Palette</a>,
          <a href="https://github.com/kgolid/chromotome" target="_blank">Chromotome</a>,
          <a href="https://www.fabiocrameri.ch/colourmaps/" target="_blank">Scientific colour maps</a>,
          <a href="https://sashamaps.net/docs/resources/20-colors/" target="_blank">Trubetskoy 20-colors</a>,
          <a href="https://github.com/morhetz/gruvbox" target="_blank">Gruvbox</a>,
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
      filterSelected: [],
      collectionSelected: null,
      colorCnt: 0
    }
  },
  computed: {
    colorsToShowChunks: function () {
      // console.log(this.sliceIntoChunks(this.colorsJson, 3));
      return this.sliceIntoChunks(this.colorList, 3);
    },
    collectionNames: function () {
      var tempCollectionNames = [];
      tempCollectionNames.push({
        value: null, text: 'Select a collection'
      });
      var uniqueCollections = new Set(this.colorsJson.map(x => x["collection"]));
      for(let collection of uniqueCollections){
        tempCollectionNames.push({
          value: collection,
          text: collection
        })
      }
      return tempCollectionNames;
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
      this.collectionSelected = null;
    },
    shuffleColorList: function () {
      this.colorList = this.colorList.sort(() => Math.random() - 0.5);
    },
    filterColorList: function () {
      console.log(this.filterSelected);
      console.log(this.collectionSelected);
      var filterSet = new Set(this.filterSelected);
      var newColorList = [];
      for(let color of this.colorsJson){
        if(this.collectionSelected !== null && this.collectionSelected !== color["collection"]){continue;}
        var colorLabels = new Set(color["labels"]);
        if(!this.isSuperset(colorLabels, filterSet)){continue;}
        if(color["colors"].length < this.colorCnt){continue;}
        newColorList.push(color);
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
