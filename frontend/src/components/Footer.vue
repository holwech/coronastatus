<template>
  <div class="footer">
    © Joachim Holwech |
    <a class="footer-link" href="https://holwech.github.io" target="_blank">Blog</a> |
    <router-link class="footer-link" to="/about">About</router-link> |
    <a class="footer-link" href="https://github.com/holwech" target="_blank">GitHub</a>
  </div>
</template>

<script lang="ts">
import { Component } from 'vue-property-decorator';
import Vue from 'vue';

@Component
export default class Footer extends Vue { }
</script>

<style>
.footer {
  background: #555555;
  color: white;
  margin-top: 70px;
  padding: 1rem;
  text-align: center;
}

.footer-link {
  color: white;
}
</style>