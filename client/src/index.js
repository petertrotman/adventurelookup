// Polyfills
import 'babel-polyfill';
import 'isomorphic-fetch';

import React from 'react';
import ReactDOM from 'react-dom';

import { AppContainer } from 'react-hot-loader';
import App from './app/App';

const rootElement = document.getElementById('main');
ReactDOM.render(<AppContainer><App /></AppContainer>, rootElement);

// Hot Reloader Config
if (module.hot) {
  module.hot.accept('./app/App', () => {
    const NextApp = require('./app/App').default;
    ReactDOM.render(<AppContainer><NextApp /></AppContainer>, rootElement);
  });
}

