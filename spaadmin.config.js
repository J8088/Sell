const path = require('path');
require("babel-polyfill");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


module.exports = {
  entry: ['babel-polyfill', './spaadmin/src/index.js'],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'spaadmin/static/spaadmin/dist/js')
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.(css|scss)$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"]
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)([\?]?.*)$/,
        use: [
          {
            loader: 'file-loader',
          }
        ]
      },
      {
        test: /\.(gif|jpe?g|png)$/,
        use: {loader: 'url-loader?limit=25000'}
      }
    ]
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css",
      chunkFilename: "[id].css"
    })
  ]
};