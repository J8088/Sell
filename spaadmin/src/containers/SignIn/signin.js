import React, {Component} from "react";
import {Link, Redirect} from "react-router-dom";
import {connect} from "react-redux";
import Input from "../../components/uielements/input";
import Checkbox from "../../components/uielements/checkbox";
import Button from "../../components/uielements/button";
import authAction from "../../redux/auth/actions";
import appAction from "../../redux/app/actions";
import IntlMessages from "../../components/intlMessages";
import SignInStyleWrapper from "./signin.style";

const {login} = authAction;
const {clearMenu} = appAction;

class SignIn extends Component {
  state = {
    redirectToReferrer: false
  };

  static getDerivedStateFromProps(props, state) {
    if (props.isLoggedIn !== state.isLoggedIn && props.isLoggedIn === true) {
      return {redirectToReferrer: true}
    }

    return state;
  }

  handleLogin = () => {
    const {login, clearMenu} = this.props;
    login();
    clearMenu();
    this.props.history.push("/spaadmin");
  };

  render() {
    const from = {pathname: "/spaadmin"};
    const {redirectToReferrer} = this.state;

    if (redirectToReferrer) {
      return <Redirect to={from} />;
    }

    return (
      <SignInStyleWrapper className="isoSignInPage">
        <div className="isoLoginContentWrapper">
          <div className="isoLoginContent">
            <div className="isoLogoWrapper">
              <Link to="/spaadmin">
                <IntlMessages id="page.signInTitle"/>
              </Link>
            </div>

            <div className="isoSignInForm">
              <div className="isoInputWrapper">
                <Input size="large" placeholder="Username"/>
              </div>

              <div className="isoInputWrapper">
                <Input size="large" type="password" placeholder="Password"/>
              </div>

              <div className="isoInputWrapper isoLeftRightComponent">
                <Checkbox>
                  <IntlMessages id="page.signInRememberMe"/>
                </Checkbox>
                <Button type="primary" onClick={this.handleLogin}>
                  <IntlMessages id="page.signInButton"/>
                </Button>
              </div>
            </div>
          </div>
        </div>
      </SignInStyleWrapper>
    );
  }
}

export default connect(
  state => ({
    isLoggedIn: state.Auth.idToken !== null ? true : false
  }),
  {login, clearMenu}
)(SignIn);
