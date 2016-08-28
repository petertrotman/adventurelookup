import React from 'react';
import { Provider } from 'react-redux';
import { Router } from 'react-router';

import routes from './routes';
import store, { history } from './store';
import './App.scss';

const App = () => (
  <Provider store={store}>
    <Router history={history} routes={routes} />
  </Provider>
);

export default App;
