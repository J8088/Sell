const path = require('path');
const webpack = require('webpack');


module.exports = {
  entry: './shop/static/js/src/main.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'shop/static/js/shop/dist')
  },
  module: {
    rules: [
      {
        test: /\.(css|scss)$/,
        use: [
          {loader: "style-loader"},
          {loader: "css-loader"},
          {loader: "sass-loader"},
          {
            loader: 'postcss-loader',
            options: {
              plugins: function () {
                return [
                  require('autoprefixer')
                ];
              }
            }
          },
        ]
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: 'fonts/dist/'
            }
          }
        ]
      },
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {}
          }
        ]
      }
    ],
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    }),
  ],
};