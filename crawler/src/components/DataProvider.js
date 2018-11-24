import React, {Component} from "react";
import PropTypes from "prop-types";

class DataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };
  state = {
    data: [],
    loaded: false,
    updateInterval: null,
    placeholder: "Loading..."
  };

  fetchData = () => {
    return fetch(this.props.endpoint)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({placeholder: "Something went wrong"});
        }
        return response.json();
      })
      .then(data => this.setState({data: data, loaded: true}));
  };

  processData(handler) {
    if (this.props.dynamic && !this.updateInterval) {
      this.updateInterval = setInterval(() => {
        handler();
      }, this.props.period * 1000);
    } else if (!this.props.dynamic && this.updateInterval) {
      clearInterval(this.updateInterval);
      this.updateInterval = null;
    }
  }

  componentDidMount() {
    this.fetchData();
  }


  render() {
    this.processData(this.fetchData);
    const {data, loaded, placeholder} = this.state;
    return loaded ? this.props.render(data) : <p>{placeholder}</p>;
  }
}

export default DataProvider;