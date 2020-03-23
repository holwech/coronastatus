<template>
  <div class="container">
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6 left" v-html="text"> </div>
      <div class="col-3"></div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import Component from 'vue-class-component';
import marked from 'marked';
import about from '@/posts/about.md';

@Component
export default class Home extends Vue {
  text = marked(about);
}
</script>
