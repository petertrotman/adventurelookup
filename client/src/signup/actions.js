export const actions = {
  SIGNUP_EMAIL: 'SIGNUP_EMAIL',
  SIGNUP_REQUEST: 'SIGNUP_REQUEST',
  SIGNUP_SUCCESS: 'SIGNUP_SUCCESS',
  SIGNUP_FAILURE: 'SIGNUP_FAILURE',
};

export function signupEmail(email, validity) {
  return (dispatch) => {
    dispatch({
      type: actions.SIGNUP_EMAIL,
      email,
      isValid: validity.valid,
    });

    if (validity.valid) {
      dispatch({
        type: actions.SIGNUP_REQUEST,
      });

      return fetch('/api/signups/', {
        method: 'POST',
        body: JSON.stringify({ email }),
        headers: { 'Content-Type': 'application/json' },
      })
        .then(response => {
          if (!response.ok) {
            throw Error(response.statusText);
          }
          return response;
        })
        .then(() => dispatch({
          type: actions.SIGNUP_SUCCESS,
        }))
        .catch(error => dispatch({
          type: actions.SIGNUP_FAILURE,
          error,
        }));
    }

    return Promise.resolve();
  };
}
