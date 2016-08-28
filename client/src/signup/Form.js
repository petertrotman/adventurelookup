import React from 'react';

class SignupForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { email: '' };
    this.changeHandler = this.changeHandler.bind(this);
    this.clickHandler = this.clickHandler.bind(this);
  }

  changeHandler(e) {
    e.preventDefault();
    this.setState({ email: e.target.value });
  }

  clickHandler(e) {
    e.preventDefault();
  }

  render() {
    return (
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
    );
  }
}

export default SignupForm;
