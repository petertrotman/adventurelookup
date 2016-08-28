import React from 'react';
import ReactDOM from 'react-dom';

import { AppContainer } from 'react-hot-loader';
import App from './App';

const rootElement = document.getElementById('main');
ReactDOM.render(<AppContainer><App /></AppContainer>, rootElement);

// Hot Reloader Config
if (module.hot) {
  module.hot.accept('./App', () => {
    const NextApp = require('./App').default;  // eslint-disable-line
    ReactDOM.render(<AppContainer><NextApp /></AppContainer>, rootElement);
  });
}

