const ip = require('ip')
const path = require('path')
const BundleTracker  = require('webpack-bundle-tracker')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

var config = {
  entry: './assets/js/main.js',
  output: {
    path: path.resolve(__dirname, 'static/bundles'),
    publicPath: '/static/bundles/',
    filename: "[name].js"
  },
  module: {
    rules: [
      // Styles.
      {test: /\.css$/, use: ['css-hot-loader', MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader']},
      {test: /\.scss$/, use: ['css-hot-loader', MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader', 'sass-loader']},
      {test: /\.sass$/, use: ['css-hot-loader', MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader', 'sass-loader?indentedSyntax']},

      // Javascript.
      {test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader'},

      // Images, media & fonts.
      {test: /\.(png|jpe?g|gif|svg)(\?.*)?$/, loader: 'url-loader', options: {limit: 10000, name: 'images/[name].[hash:7].[ext]'}},
      {test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/, loader: 'url-loader', options: {limit: 10000, name: 'media/[name].[hash:7].[ext]'}},
      {test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/, loader: 'url-loader', options: {limit: 10000, name: 'fonts/[name].[hash:7].[ext]'}}
    ]
  },
  plugins: [
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({filename: '[name].css'})
  ],
  devServer: {
    headers: {'Access-Control-Allow-Origin': '*'},
    historyApiFallback: true,
    host: '0.0.0.0',
    port: 3000,
    stats: 'minimal'
  }
}

module.exports = (env, argv) => {
  if (argv.mode === 'development') {
    config.output.publicPath = `http://${ip.address()}:3000/static/bundles/`
    config.plugins = (config.plugins || []).concat([
      new BundleTracker({filename: './static/webpack-stats-dev.json'})
    ])
  }

  if (argv.mode === 'production') {
    config.plugins = (config.plugins || []).concat([
      new BundleTracker({filename: './static/webpack-stats.json'})
    ])
  }

  return config
}
