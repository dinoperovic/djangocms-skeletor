var ip = require('ip')
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  context: __dirname,
  entry: './assets/js/main.js',
  output: {
    path: path.resolve('./static/bundles/'),
    filename: "[name].js"
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader!postcss-loader'
        }))
      },
      {
        test: /\.scss$/,
        use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader!postcss-loader!sass-loader'
        }))
      },
      {
        test: /\.sass$/,
        use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader!postcss-loader!sass-loader?indentedSyntax'
        }))
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: 'images/[name].[hash:7].[ext]'
        }
      },
      {
        test: /\.(mp4|webm|ogg|mp3|wav|flac|aac)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: 'media/[name].[hash:7].[ext]'
        }
      },
      {
        test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
        loader: 'url-loader',
        options: {
          limit: 10000,
          name: 'fonts/[name].[hash:7].[ext]'
        }
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin('style.css')
  ],
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    host: '0.0.0.0',
    port: 3000,
    headers: {'Access-Control-Allow-Origin': '*'}
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'development') {
  module.exports.output.publicPath = `http://${ip.address()}:3000/static/bundles/`
  module.exports.plugins = (module.exports.plugins || []).concat([
    new BundleTracker({filename: './static/webpack-stats-dev.json'})
  ])
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  module.exports.output.publicPath = '/static/bundles/'
  module.exports.plugins = (module.exports.plugins || []).concat([
    new BundleTracker({filename: './static/webpack-stats.json'}),
    new webpack.DefinePlugin({'process.env': {NODE_ENV: '"production"'}}),
    new webpack.optimize.UglifyJsPlugin({sourceMap: true, compress: {warnings: false}}),
    new webpack.LoaderOptionsPlugin({minimize: true})
  ])
}
