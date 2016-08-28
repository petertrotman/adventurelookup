import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux';

import signupReducer from './signup/reducer';

const reducer = combineReducers({
  routing: routerReducer,
  signup: signupReducer,
});

export default reducer;
