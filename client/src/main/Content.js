import React from 'react';

const Content = props => (
  <div className="content-container">
    <div className="content">
      { props.children }
    </div>
  </div>
);

Content.propTypes = {
  children: React.PropTypes.any,
};

export default Content;
