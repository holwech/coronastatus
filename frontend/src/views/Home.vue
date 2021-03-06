<template>
  <div>
    <div class="headline">
      <h1>COVID-19 daily update</h1> (Last updated: {{stats['last_updated']}})
    </div>
    <div class="container">
      <div class="data-element">
        <div class="row">
          <div class="col-12">
            <div class="row">
              <div class="col-12">
                <h2 style="margin:0px;">Summary
                  <Tooltip>
                    Legend: <br>
                    - Yesterday's reported numbers<br>
                    <span style="color:red;"> - Change from day before</span>
                  </Tooltip>
                </h2>
              </div>
            </div>
            <hr>
          </div>
        </div>
        <div class="row">
          <!-- Big numbers -->
          <div class="col-12">
            <div class="row">
              <div class="col-3 single-number-container">
                <h1 class="single-number">{{stats["total_confirmed"]}}</h1>
                <span style="color:red;">+{{stats["total_confirmed_change"]}}</span>
                <p class='small-text'>Total confirmed positive<br/></p>
              </div>
              <div class="col-3 single-number-container">
                <h1 class="single-number">{{stats["num_countries_over_limit_confirmed"]}}</h1>
                <span style="color:red;">+{{stats["num_countries_over_limit_confirmed_change"]}}</span>
                <p class='small-text'>Countries with more than 500 confirmed positive<br/></p>
              </div>
              <div class="col-3 single-number-container">
                <h1 class="single-number">{{stats["total_deaths"]}}</h1>
                <span style="color:red;">+{{stats["total_deaths_change"]}}</span>
                <p class='small-text'>Total deaths globally<br/></p>
              </div>
              <div class="col-3 single-number-container">
                <h1 class="single-number">{{stats["num_countries_over_5_deaths"]}}</h1>
                <span style="color:red;">+{{stats["num_countries_over_5_deaths_change"]}}</span>
                <p class='small-text'>Countries with more than 5 deaths<br/></p>
              </div>
            </div>
          </div>
        </div>
        <hr>
        <div class="row">
          <div class="col-12">
            <div class="row">
              <div class="col-12">
                <h3 style="margin:0px;">Top 6 countries ordered by new fatalities
                  <Tooltip>
                    Legend: <br>
                    - Country name <br>
                    - Yesterday's total reported deaths <br>
                    <span style="color:red;"> - Change from day before</span>
                  </Tooltip>
                </h3>
              </div>
            </div>
            <hr>
          </div>
        </div>
        <!-- Country summary -->
        <div class="row">
          <div class="col-2" v-for="item in countryStats" :key="item[0]">
            <h3 class="single-number">{{item[0]}}</h3>
            <p style="font-size:20px;">{{item[1]}}</p>
            <span style="color:red;font-size:15px;">+{{item[2]}}</span>
          </div>
        </div>
        <hr />
        <!-- Status plot -->
        <div class="row">
          <div class="col-8" id="status-plot"></div>
          <div class="col-4" id="status-plot-pie-chart" style="border-left: 1px solid lightgray;margin:-1px;"></div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 center" style="padding-bottom: 50px;"><span class="material-icons" style="font-size: 100px;">keyboard_arrow_down</span></div>
      </div>
      <DataElement figureName="top_deaths_per_time">
        <div class="left" v-html="content[8]"></div>
        <template v-slot:footer>
          <p v-if="isMobile" style="color:red;">
            For mobile users - Click the lines to reveal country.
          </p>
        </template>
      </DataElement>
      <DataElement figureName="figure_1">
        <div class="left" v-html="content[0]"></div>
        <template v-slot:footer>
          <p v-if="isMobile" style="color:red;">
            For mobile users - Click the lines to reveal country.
          </p>
        </template>
      </DataElement>
      <DataElement figureName="figure_2">
        <div class="left" v-html="content[1]"></div>
      </DataElement>
      <DataElement figureName="daily_change">
        <div class="left" v-html="content[5]"></div>
      </DataElement>
      <DataElement figureName="daily_change2">
        <div class="left" v-html="content[6]"></div>
      </DataElement>
      <DataElement figureName="figure_3">
        <div class="left" v-html="content[2]"></div>
      </DataElement>
      <DataElement figureName="figure_4">
        <div class="left" v-html="content[3]"></div>
      </DataElement>
      <DataElement figureName="peak_deaths">
        <div class="left" v-html="content[7]"></div>
      </DataElement>
      <DataElement figureName="figure_5">
        <div class="left" v-html="content[4]"></div>
      </DataElement>
      <div class="row">
        <div class='col-12'>
          <Disqus></Disqus>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import data from '../data/data.json';
import Vue from 'vue';
import Component from 'vue-class-component';
import DataElement from '@/components/DataElement';
import Disqus from '@/components/Disqus';
import marked from 'marked';
import Tooltip from '@/components/Tooltip';
import { insertPlot } from '@/utils/plotting';
import info1 from '@/posts/info1.md';
import info2 from '@/posts/info2.md';
import info3 from '@/posts/info3.md';
import info4 from '@/posts/info4.md';
import info5 from '@/posts/info5.md';
import dailyChange from '@/posts/daily_change.md';
import dailyChange2 from '@/posts/daily_change2.md';
import topDaily from '@/posts/top_daily.md'
import peak from '@/posts/peak.md';

@Component({
  components: {
    DataElement,
    Disqus,
    Tooltip
  }
})
export default class Home extends Vue {
  stats = data['stats'];
  isMobile = false;
  content = [info1, info2, info3, info4, info5, dailyChange, dailyChange2, peak, topDaily].map(info => marked(info));

  get countryStats() {
    return Object.entries(this.stats['change_deaths'])
                 .slice(0,6)
                 .map((el) => [el[0], this.stats['deaths'][el[0]], el[1]]);
  }

  mounted() {
    this.isMobile = window.screen.availWidth < 800;
    insertPlot('deaths_area', data, 'status-plot');
    insertPlot('deaths_pie_chart', data, 'status-plot-pie-chart');
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