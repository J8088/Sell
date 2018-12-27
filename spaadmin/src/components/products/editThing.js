import React, {Component} from 'react';
import Scrollbar from 'react-smooth-scrollbar';
import {Map} from 'immutable';
import Async from '../../helpers/asyncComponent';
import Button from '../uielements/button';
import {Layout, Icon, Form} from "antd";
import ClearButton from "./clearButton";
import Input from '../uielements/input';
import notification from '../notification';
import IntlMessages from '../intlMessages';
import EditProductView from './editView';
import EditThingWrapper from './editThing.style';


export default class EditThing extends Component {
  constructor(props) {
    super(props);
    this.state = {
      thing: {},
      editorState: null,
      loading: false,
      iconLoading: false
    };
  }

  handleInputChange = (e) => {
    this.props.handleInputChange(e.target);
  };

  handleCategoriesCheckBoxChange = (e) => {
    this.props.handleCategoriesCheckBoxChange(e.target);
  };

  handleFiltersCheckBoxChange = (e) => {
    this.props.handleFiltersCheckBoxChange(e.target);
  };

  render() {
    const {thing, handleSaveThing, handleImageChange, handleCloseThing, categories, filters} = this.props;

    const closeProduct = () => {
      handleCloseThing()
    };

    const refreshProduct = (productId) => {
      this.props.handleRefreshThing(productId);
    };

    const otherAttributes = () => {
    };

    return (
      <EditThingWrapper className="sellComposeProductWrapper">
        <Form onSubmit={handleSaveThing}>
          <div className="isoContactControl">
            <Button type="primary" htmlType="submit">
              <Icon type="check"/>{" "}
            </Button>
            <ClearButton
              clearProduct={closeProduct}
              product={thing}
            />
            <Button type="primary" onClick={() => refreshProduct(thing.product_id)} className="isoAddContactBtn">
              <IntlMessages id="product.refreshProduct"/>
            </Button>
          </div>
          <Scrollbar className="contactBoxScrollbar">
            <EditProductView
              product={thing}
              categories={categories}
              filters={filters}
              handleImageChange={handleImageChange}
              handleInputChange={this.handleInputChange}
              handleFiltersCheckBoxChange={this.handleFiltersCheckBoxChange}
              handleCategoriesCheckBoxChange={this.handleCategoriesCheckBoxChange}
              otherAttributes={otherAttributes}
            />
          </Scrollbar>
        </Form>
      </EditThingWrapper>
    );
  }
}
