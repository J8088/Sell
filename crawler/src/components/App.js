import React from "react";
import ReactDOM from "react-dom";
import Dashboard from "./Dashboard"

const App = () => (
  <Dashboard />
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App/>, wrapper) : null;