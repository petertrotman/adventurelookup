import React from 'react';

const Footer = props => (
  <div className="footer">
    { props.children }
  </div>
);

Footer.propTypes = {
  children: React.PropTypes.any,
};

export default Footer;
