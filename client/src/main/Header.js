import React from 'react';

const Header = props => (
  <div className="header">
    { props.children }
  </div>
);

Header.propTypes = {
  children: React.PropTypes.any,
};

export default Header;
