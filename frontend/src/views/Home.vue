<template>
  <div>
    <div class="headline">
      <h1>COVID-19 daily update</h1>
    </div>
    <div class="container">
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <h2>Looking at confirmed cases of COVID-19</h2>
            <p>
              Looking at the confirmed cases of COVID-19, it might seem the situation in China is significantly more severe than the rest of the world.
              As we will see below, the reality is much different...
              <br /><br /> NOTE: The plots are interactive and exploration is encouraged! Click on the legend names to toggle lines off or on.
            </p>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" id="plot1"></div>
        </div>
      </div>
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <h2>Lack of good data</h2>
            <p>
              Looking at the confirmed cases of COVID-19, it might seem the situation in China is significantly more severe than the rest of the world.
              As we will see below, the reality is much different...
              <br /><br /> NOTE: The plots are interactive and exploration is encouraged!
            </p>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" id="plot2"></div>
        </div>
      </div>
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <h2>Looking at confirmed cases of COVID-19</h2>
            <p>
              Looking at the confirmed cases of COVID-19, it might seem the situation in China is significantly more severe than the rest of the world.
              As we will see below, the reality is much different...
              <br /><br /> NOTE: The plots are interactive and exploration is encouraged!
            </p>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" id="plot3"></div>
        </div>
      </div>
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <h2>Looking at confirmed cases of COVID-19</h2>
            <p>
              Looking at the confirmed cases of COVID-19, it might seem the situation in China is significantly more severe than the rest of the world.
              As we will see below, the reality is much different...
              <br /><br /> NOTE: The plots are interactive and exploration is encouraged!
            </p>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" id="plot4"></div>
        </div>
      </div>
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <h2>Looking at confirmed cases of COVID-19</h2>
            <p>
              Looking at the confirmed cases of COVID-19, it might seem the situation in China is significantly more severe than the rest of the world.
              As we will see below, the reality is much different...
              <br /><br /> NOTE: The plots are interactive and exploration is encouraged!
            </p>
            <hr>
          </div>
        </div>
        <div class="row">
          <div class="col-12" id="plot5"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import plotly from 'plotly.js-dist';
import data from '../data/data.json';
import Vue from 'vue';
import Component from 'vue-class-component';

@Component
export default class Home extends Vue {
  mounted() {
    this.insertPlot(1, data);
    this.insertPlot(2, data);
    this.insertPlot(3, data);
    this.insertPlot(4, data);
    this.insertPlot(5, data);
  }

  insertPlot(number, data) {
    const plot = JSON.parse(data['plots'][`figure_${number}`]);
    if (window.screen.availWidth < 800) {
      plot['layout']['showlegend'] = false;
    }
    plot['config'] = {
      responsive: true,
    }
    plotly.newPlot(`plot${number}`, plot);
  }
}
</script>

<style>
.item-style {
  height: 600px;
}

.data-element {
  border: 1px solid lightgray;
  margin-bottom: 50px;
}

hr {
  border: 0.5px solid lightgray;
}
</style>