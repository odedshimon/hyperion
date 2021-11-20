<template>
  <div class="home">
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous" />
        <title>Hyperion OSINT System</title>
    </head>
    <h3>Enter domain name</h3>
    <input type="text" name="domain-text-box" id="domain-text-box" ref="domain">
    <button @click="fetchData">Fetch</button>
    <div class="reults-container">
      <json-viewer :value="whoisData"></json-viewer>
      <json-viewer :value="dnsData"></json-viewer>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import JsonViewer from 'vue-json-viewer'

const backendURL = "http://localhost:5000/whois?domain="

Vue.use(JsonViewer)

export default {
  props: {
  },
  data(){
    return{
      domain: '',
      whoisData: '',
      dnsData: ''
    }
  },
  methods: {
    fetchData: async function(){
      this.domain = this.$refs.domain.value
      console.log("Sending request to backend")
      const whoisResponse = await axios.get(backendURL + this.domain)
      this.whoisData = whoisResponse.data
      console.log("Response accepted from backend")
    }
  }
}
</script>

<style>
.home{
  margin-left: 30px;
}
.jv-number-float {
  color: #faa !important;
}
.jv-key-node {
  display: flex;
}
.reults-container {
  display: flex;
}
</style>