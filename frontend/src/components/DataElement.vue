<template>
  <div class="data-element">
    <div class="row">
      <div class="col-12">
        <slot></slot>
        <slot name="footer"></slot>
      </div>
    </div>
    <div class="row">
      <div class="col-12" :id="`plot_${figureName}`"></div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component, Prop } from 'vue-property-decorator';
import data from '../data/data.json';
import { insertPlot } from '@/utils/plotting';

@Component
export default class DataElement extends Vue {
  @Prop(String) readonly figureName!: string;
  stats = data['stats'];
  isMobile = false;

  mounted() {
    this.isMobile = window.screen.availWidth < 800;
    insertPlot(this.figureName, data, `plot_${this.figureName}`, this.isMobile);
  }
}
</script>

<style>
.data-element {
  border: 1px solid lightgray;
  margin-bottom: 50px;
}
</style>