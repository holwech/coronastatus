<template>
  <div>
    <div class="headline">
      <h1>COVID-19 daily update</h1>
    </div>
    <div class="container">
      <div class="data-element">
        <div class="row">
          <div class="row">
            <div class="col-12 center">
              <h2 style="margin:0px;">Summary</h2>
              <hr>
            </div>
          </div>
          <!-- Big numbers -->
          <div class="col-6">
            <div class="row">
              <div class="col-6 single-number-container">
                <h1 class="single-number">{{stats["num_countries_over_5_deaths"]}}</h1>
                <span style="color:red;">+{{stats["num_countries_over_5_deaths_change"]}}</span>
                <p class='small-text'>countries with more than 5 deaths<br/></p>
              </div>
              <div class="col-6">
                <h1 class="single-number">{{stats["total_deaths"]}}</h1>
                <span style="color:red;">+{{stats["total_deaths_change"]}}</span>
                <p class='small-text'>Total deaths globally<br/></p>
              </div>
            </div>
          </div>
          <div class="col-6">
            <div class="row">
              <div class="col-12">
                <h3 style="margin:0px;">Status</h3>
                <p style="font-size:16px;">
                  Steep increase for Italy, Spain and France. US and UK following behind with about a 2 weeks delay.
                </p>
              </div>
            </div>
          </div>
        </div>
        <!-- Country summary -->
        <div class="row">
          <div class="col-2" v-for="item in countryStats" :key="item[0]">
            <h2 class="single-number">{{item[0]}}</h2>
            <p style="font-size:20px;">{{item[1]}}<br/></p>
            <span style="color:red;font-size:15px;">+{{stats["total_deaths_change"]}}</span>
          </div>
        </div>
        <!-- Status plot -->
        <div class="row">
          <div class="col-12" id="status-plot"> </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 center" style="padding-bottom: 50px;"><span class="material-icons" style="font-size: 100px;">keyboard_arrow_down</span></div>
      </div>
      <DataElement :num="1">
        <div v-html="content[0]"></div>
        <template v-slot:footer>
          <p v-if="isMobile" style="color:red;">
            For mobile users - Click the lines to reveal country.
          </p>
        </template>
      </DataElement>
      <DataElement :num="2">
        <div v-html="content[1]"></div>
      </DataElement>
      <DataElement :num="3">
        <div v-html="content[2]"></div>
      </DataElement>
      <DataElement :num="4">
        <div v-html="content[3]"></div>
      </DataElement>
      <DataElement :num="5">
        <div v-html="content[4]"></div>
      </DataElement>
    </div>
  </div>
</template>

<script>
import data from '../data/data.json';
import Vue from 'vue';
import Component from 'vue-class-component';
import DataElement from '@/components/DataElement';
import marked from 'marked';
import { insertPlot } from '@/utils/plotting';
import info1 from '@/posts/info1.md';
import info2 from '@/posts/info2.md';
import info3 from '@/posts/info3.md';
import info4 from '@/posts/info4.md';
import info5 from '@/posts/info5.md';

@Component({
  components: {
    DataElement
  }
})
export default class Home extends Vue {
  stats = data['stats'];
  isMobile = false;
  content = [info1, info2, info3, info4, info5].map(info => marked(info));

  get countryStats() {
    return Object.entries(this.stats['deaths'])
                 .slice(0,6)
                 .map((el) => [el[0], el[1], this.stats['change_deaths'][el[0]]]);
  }

  mounted() {
    this.isMobile = window.screen.availWidth < 800;
    insertPlot(2, data, 'status-plot', this.isMobile);
  }
}
</script>

<style>
.item-style {
  height: 600px;
}

hr {
  border: 0.5px solid lightgray;
}

.small-text {
  font-size: 15px;
}

.single-number-container {
  padding: 0px;
}

.single-number {
  margin: 0px;
}

.modebar {
  display: none;
}
</style>