import React from 'react';
import { Route, IndexRoute } from 'react-router';

import About from './about/About';
import Adventures from './adventures/Adventures';
import Main from './main/Main';
import Signup from './signup/Signup';

const routes = (
  <Route path="/" component={Main}>
    <IndexRoute component={Signup} />
    <Route path="about" component={About} />
    <Route path="adventures" component={Adventures} />
    <Route path="signup" component={Signup} />
  </Route>
);

export default routes;
