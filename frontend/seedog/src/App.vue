<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <!-- <Home></Home> -->
<RouterView></RouterView>
</template>

<script>
import { RouterView } from 'vue-router';

// import Home from "./components/Home.vue"
// import Login from "./components/Login.vue";
export default {
    name: 'App'
    // components:{
    //   Login
    // }
    ,
    components: { RouterView }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2d86df;
  /* background-color: #7d5dc7; */
}
body{
  background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
  height: 100vh;
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0;
}
</style>
