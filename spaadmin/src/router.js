import React from "react";
import {Route, Redirect, Switch} from "react-router-dom";
import {connect} from "react-redux";
import App from "./containers/App/App";
import {ConnectedRouter} from 'connected-react-router';
import asyncComponent from "./helpers/AsyncFunc";

const RestrictedRoute = ({component: Component, isLoggedIn, ...rest}) => {
  return (
    <Route
      {...rest}
      render={props =>
        isLoggedIn ? (
          <Component {...props} />
        ) : (
          <Redirect
            to={{
              pathname: "/spaadmin/signin",
              state: {from: props.location}
            }}
          />
        )
      }
    />
  )
};

const PublicRoutes = ({history, isLoggedIn}) => {
  return (
    <ConnectedRouter history={history}>
      <Switch>
        <Route
          exact
          path={"/spaadmin/signin"}
          component={asyncComponent(() => require("./containers/SignIn/signin"))}
        />
        <RestrictedRoute
          path="/spaadmin"
          component={App}
          isLoggedIn={isLoggedIn}
        />
      </Switch>
    </ConnectedRouter>

  );
};

export default connect(state => {
  return ({
    isLoggedIn: state.Auth.idToken !== null
  })
})(PublicRoutes);
