import React from 'react';
import { connect } from 'react-redux';

import { signupEmail } from './actions';

@connect(
  state => ({ signup: state.signup }),
  dispatch => ({ submitEmail: (email, validity) => (
    dispatch(signupEmail(email, validity))
  ) }),
)
class SignupForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { email: this.props.signup.email, validity: {} };
    this.changeHandler = this.changeHandler.bind(this);
    this.clickHandler = this.clickHandler.bind(this);
  }

  changeHandler(e) {
    e.preventDefault();
    this.setState({
      email: e.target.value,
      validity: e.target.validity,
    });
  }

  clickHandler(e) {
    e.preventDefault();
    this.props.submitEmail(this.state.email, this.state.validity);
  }

  render() {
    return (
      <div className="signup-form">
        <form>
          <input
            type="email"
            value={this.state.email || ''}
            onChange={this.changeHandler}
          />
          <button
            type="submit"
            onClick={this.clickHandler}
          >
            Sign Up
          </button>
        </form>
        <div>
          { this.props.signup.isValid
            ? null
            : <span className="warning">Not a valid e-mail address.</span>
          }
          { this.props.signup.completed
            ? <span className="success">You have successfully signed up!</span>
            : null
          }
        </div>
      </div>
    );
  }
}

SignupForm.propTypes = {
  signup: React.PropTypes.object,
  submitEmail: React.PropTypes.func,
};

export default SignupForm;
