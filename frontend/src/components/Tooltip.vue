<template>
  <div class="tooltip">
    <span class="material-icons">info</span>
    <p class="tooltiptext"><slot>Tooltip text</slot></p>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'vue-property-decorator';

@Component
export default class Tooltip extends Vue { }
</script>

<style>
.tooltip {
  position: relative;
  display: inline-block;
}

/* Tooltip text */
.tooltip .tooltiptext {
  display: none;
  width: auto;
  white-space: nowrap;
  text-align: left;
  background-color: #FFFDFB;
  color: #333447;
  padding: 2px;
  border-radius: 2px;
  border: solid 1px #333447;
  font-size: 12px;

  position: absolute;
  z-index: 1;
  top: -43px;
  right: 105%;
}

.tooltip .tooltiptext::after {
  content: " ";
  position: absolute;
  top: 50%;
  left: 100%; /* To the right of the tooltip */
  margin-top: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent transparent  #333447;
}

.tooltip:hover .tooltiptext {
  display: block;
  opacity: 1;
}
</style>