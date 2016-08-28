import { actions } from './actions';

const defaultState = {
  email: '',
  completed: false,
  isFetching: false,
  isValid: true,
};

export default function reducer(state = defaultState, action) {
  switch (action.type) {
    case actions.SIGNUP_EMAIL:
      return Object.assign({}, state, {
        email: action.email,
        isValid: action.isValid,
      });

    case actions.SIGNUP_REQUEST:
      return Object.assign({}, state, { isFetching: true });

    case actions.SIGNUP_SUCCESS:
    case actions.SIGNUP_FAILURE:
      return Object.assign({}, state, {
        isFetching: false,
        completed: true, // Don't want user to know on failure for privacy
      });

    default:
      return state;
  }
}
