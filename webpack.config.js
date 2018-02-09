var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,
  entry: ['./assets/js/main.js'],
  output: {
    path: path.resolve('./static/bundles/'),
    filename: "[name]-[hash].js"
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    port: 3000
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'development') {
  module.exports.entry = module.exports.entry.concat(['webpack-dev-server/client?http://localhost:3000'])
  module.exports.output.publicPath = 'http://localhost:3000/static/bundles/'
  module.exports.plugins = (module.exports.plugins || []).concat([
    new BundleTracker({filename: './webpack-stats-dev.json'})
  ])
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  module.exports.plugins = (module.exports.plugins || []).concat([
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.DefinePlugin({'process.env': {NODE_ENV: '"production"'}}),
    new webpack.LoaderOptionsPlugin({minimize: true})
  ])
}
