import React from 'react';

import Content from './Content';
import Footer from './Footer';
import Header from './Header';
import Nav from './Nav';

import './Main.scss';

const Main = props => (
  <div>
    <Header>
      <Nav />
    </Header>
    <Content>
      { props.children }
    </Content>
    <Footer />
  </div>
);

Main.propTypes = {
  children: React.PropTypes.any,
};

export default Main;
