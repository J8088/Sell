const path = require('path');
require("babel-polyfill");

module.exports = {
  entry: ['babel-polyfill', './crawler/src/index.js'],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'crawler/static/js/crawler/dist')
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};

//    "dev": "webpack --mode development ./project/frontend/src/index.js --output ./project/frontend/static/frontend/main.js",