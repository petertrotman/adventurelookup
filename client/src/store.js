import { createStore, applyMiddleware, compose } from 'redux';
import { browserHistory } from 'react-router';
import { syncHistoryWithStore } from 'react-router-redux';
import createLogger from 'redux-logger';
import thunk from 'redux-thunk';

import reducer from './reducer';

const defaultState = {};
const logger = createLogger();

const store = createStore(
  reducer,
  defaultState,
  compose(
    applyMiddleware(thunk, logger),
    window.devToolsExtension ? window.devToolsExtension() : f => f
  )
);

// React Hot Reloader config
if (module.hot) {
  module.hot.accept('./reducer', () => {
    const nextReducer = require('./reducer').default;  // eslint-disable-line
    store.replaceReducer(nextReducer);
  });
}

export const history = syncHistoryWithStore(browserHistory, store);
export default store;
