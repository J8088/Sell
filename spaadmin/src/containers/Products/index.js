import React, {Component} from "react";
import {connect} from "react-redux";
import DesktopView from "./desktopView";
import MobileView from "./mobileView";
import TabView from "./tabView";

class Products extends Component {
  render() {
    const {view, height} = this.props;
    const ProductView =
      view === "DesktopView"
        ? DesktopView
        : view === "TabView" ? TabView : MobileView;
    return (
      <div style={{height: "100%"}}>
        <ProductView height={height}/>
      </div>
    );
  }
}

export default connect(state => ({
  ...state.App
}))(Products);
