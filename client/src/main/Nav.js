import React from 'react';
import { Link } from 'react-router';

const NavLink = props => (
  <Link className="nav-link" {...props}>{ props.children }</Link>
);

NavLink.propTypes = {
  to: React.PropTypes.string,
  children: React.PropTypes.any,
};

const Nav = () => (
  <nav className="nav-main">
    <div className="nav-left">
      <NavLink to="/">Adventure Lookup</NavLink>
    </div>
    <div className="nav-right">
      <NavLink to="/adventures">Adventures</NavLink>
      <NavLink to="/about">About</NavLink>
    </div>
  </nav>
);

export default Nav;

