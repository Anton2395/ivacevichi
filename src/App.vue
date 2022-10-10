<template>
  <router-view/>
</template>

<style lang="scss">
html {
  width: 100%;
  height: 100%;
}
body {
  width: 100%;
  height: 100%;
  
  font-family: 'Lato';
}
* {
  border: 0;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
@font-face {
  font-family: "Lato";
  // src: local("Lato"),
  //  url(./fonts/Lato/Lato-Semibold.ttf) format("truetype");
  src: url('./fonts/Lato/Lato-Medium.woff2') format('woff2'), url('./fonts/Lato/Lato-Medium.woff') format('woff');
  font-weight: 500;
	font-style: normal;
	
}
@font-face {
  font-family: "Open Sans";
  src: url('./fonts/Lato/Lato-Medium.woff2') format('woff2'), url('./fonts/Lato/Lato-Medium.woff') format('woff');
  font-weight: 500;
	font-style: normal;
}
#app {
  width: 100%;
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
