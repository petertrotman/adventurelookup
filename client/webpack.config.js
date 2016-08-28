/* global __dirname */
const autoprefixer = require('autoprefixer');
const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

let config = {
  entry: [
    'react-hot-loader/patch',
    './src/index.js'
  ],
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js',
    publicPath: '/static/'
  },
  resolve: {
    extensions: ['', '.js']
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel',
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        loaders: ['style', 'css', 'postcss'],
      },
      {
        test: /(\.scss|\.sass)$/,
        loaders: ['style', 'css', 'postcss', 'sass']
      },
      {
        test: /\.woff$/,
        loader: "url-loader?limit=10000&mimetype=application/font-woff&name=[path][name].[ext]"
      },
      {
        test: /\.woff2$/,
        loader: "url-loader?limit=10000&mimetype=application/font-woff2&name=[path][name].[ext]"
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2)$/,
        loader: 'file?name=[path][name].[ext]'
      },
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Adventure Lookup',
      template: './src/index.html.ejs'
    }),
  ],
  postcss: [
    autoprefixer,
  ],
};

if (process.env.NODE_ENV === 'production') {
  config = Object.assign(config, {
    plugins: config.plugins.concat(
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('production')
        }
      }),
      new webpack.optimize.OccurrenceOrderPlugin(),
      new webpack.optimize.DedupePlugin(),
      new webpack.optimize.UglifyJsPlugin()
    )
  });
}
else {
  config = Object.assign(config, {
    debug: true,
    devtool: 'source-map',
    output: Object.assign(config.output, { pathinfo: true }),
    plugins: config.plugins.concat(
      new webpack.DefinePlugin({
        'process.env': {
          'NODE_ENV': JSON.stringify('development')
        }
      })
    ),
    devServer: {
      contentBase: './dist',
      historyApiFallback: true,
      host: '0.0.0.0',
      port: 80,
      stats: 'errors-only',
    }
  });
}

module.exports = config;
