module.exports = {
  productionSourceMap: false,
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import "@/scss/constants.scss";
        `
      }
    }
  }
};
