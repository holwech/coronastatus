<template>
  <div>
    <div class="headline">
      <h1>Corona status</h1>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-10" id="plot"></div>
        <div class="col-2">Test</div>
      </div>
    </div>
  </div>
</template>

<script>
import plotly from 'plotly.js-dist';
import plots from '../data/data.json';
import Vue from 'vue';
import Component from 'vue-class-component';

@Component
export default class Home extends Vue {
  mounted() {
    console.log(plots['figure_1']);
    const plot = JSON.parse(plots['plots']['figure_1']);
    plot['config'] = {
      responsive: true,
    }
    plotly.newPlot('plot', plot);
  }
}
</script>

<style>
.item-style {
  height: 600px;
}
</style>