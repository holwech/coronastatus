<template>
  <div>
    <div class="headline">
      <h1>Corona status</h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-6" id="plot"></div>
        <div class="col-6"></div>
      </div>
    </div>
  </div>
</template>

<script>
import plotly from 'plotly.js-dist';
import plots from '../plots/test_corona.json';
import Vue from 'vue';
import Component from 'vue-class-component';

@Component
export default class Home extends Vue {
  mounted() {
    console.log(plots);
    const plot = JSON.parse(plots['test']);
    plot['config'] = {
      responsive: true,
    }
    plotly.newPlot('plot', plot);
  }
}
</script>

<style>
.item-style {
  height: 500px;
}
</style>