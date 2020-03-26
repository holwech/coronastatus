<template>
  <div id="disqus_thread" style="padding:10px;"></div>
</template>

<script>
import { Component } from 'vue-property-decorator';
import Vue from 'vue';

@Component()
export default class Disqus extends Vue {
  mounted() {
    const disqus_config = function () { // eslint-disable-line
      this.page.url = window.location.href;  // Replace PAGE_URL with your page's canonical URL variable
      this.page.identifier = 'covid19'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    const d = document, s = d.createElement('script');
    s.src = 'https://pandemicstatus.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
  }
}
</script>