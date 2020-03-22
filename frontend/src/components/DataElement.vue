<template>
  <div class="data-element">
    <div class="row">
      <div class="col-12">
        <slot></slot>
        <slot name="footer"></slot>
        <hr>
      </div>
    </div>
    <div class="row">
      <div class="col-12" :id="`plot${num}`"></div>
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
  @Prop(Number) readonly num!: number;
  stats = data['stats'];
  isMobile = false;

  mounted() {
    this.isMobile = window.screen.availWidth < 800;
    insertPlot(this.num, data, undefined, this.isMobile);
  }
}
</script>

<style>
.data-element {
  border: 1px solid lightgray;
  margin-bottom: 50px;
}
</style>