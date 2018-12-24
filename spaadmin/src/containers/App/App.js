import React, {Component} from 'react';
import {connect} from 'react-redux';
import {Layout} from 'antd';
import {Debounce} from 'react-throttle';
import WindowResizeListener from 'react-window-size-listener';
import appActions from '../../redux/app/actions';
import AppRouter from './AppRouter';
import Sidebar from '../Sidebar/Sidebar';
import {AppLocale} from '../../dashApp';
import AppHolder from './commonStyle';
import './global.css';

const {Content, Footer} = Layout;
const {toggleAll} = appActions;

export class App extends Component {
  render() {
    const {url} = this.props.match;
    const {height} = this.props;
    const appHeight = window.innerHeight;
    return (
      <AppHolder>
        <Layout style={{height: appHeight}}>
          <Debounce time="1000" handler="onResize">
            <WindowResizeListener
              onResize={windowSize => {
                return this.props.toggleAll(
                  windowSize.windowWidth,
                  windowSize.windowHeight
                )
              }
              }
            />
          </Debounce>
          <Layout style={{flexDirection: 'row', overflowX: 'hidden'}}>
            <Sidebar url={'/spaadmin'}/>
            <Layout
              className="isoContentMainLayout"
              style={{
                height: height
              }}
            >
              <Content
                className="isomorphicContent"
                style={{
                  flexShrink: '0',
                  background: '#f1f3f6',
                  position: 'relative'
                }}
              >
                <AppRouter url={url}/>
              </Content>
            </Layout>
          </Layout>
        </Layout>
      </AppHolder>
    )
  }
}


export default connect(
  state => ({
    auth: state.Auth,
    height: state.App.height
  }),
  {toggleAll}
)(App);