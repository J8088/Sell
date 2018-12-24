import React, {Component} from 'react';
import {Route} from 'react-router-dom';
import asyncComponent from '../../helpers/AsyncFunc';

const routes = [
  {
    path: 'products',
    component: asyncComponent(() => require('../Products')),
  },
  {
    path: 'settings',
    component: asyncComponent(() => require('../Settings')),
  },
];

class AppRouter extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const {url, style} = this.props;
    return (
      <div style={style}>
        {routes.map(singleRoute => {
          const {path, exact, ...otherProps} = singleRoute;
          return (
            <Route
              exact={exact === false ? false : true}
              key={path}
              path={`${url}/${path}`}
              {...otherProps}
            />
          );
        })}
      </div>
    );
  }
}

export default AppRouter;
