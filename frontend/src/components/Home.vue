<template>
  <div class="hello">
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous" />
        <title>Hyperion OSINT System</title>
    </head>
    <h3>Enter domain name</h3>
    <input type="text" name="domain-text-box" id="domain-text-box">
    <button @click="fetchData">Fetch</button>
    <label>{{ whoisData }}</label>
  </div>
</template>

<script>
import axios from 'axios'

const backendURL = "http://localhost:5000/whois?domain="

export default {
  props: {
  },
  data(){
    return{
      whoisData: [],
      domain: ""
    }
  },
  methods: {
    fetchData: async function(){
      this.domain = document.getElementById('domain-text-box').value
      console.log("Sending request to backend")
      const response = await axios.get(backendURL + this.domain)
      this.whoisData = response.data
      console.log("Response accepted from backend")
    }
  }
}
</script>

