import React, { Component } from 'react';
import IntlMessages from '../intlMessages';
import ProductComposeBtnWrapper from './productComposeBtn.style';

export default class extends Component {
  render() {
    return (
      <ProductComposeBtnWrapper className="isoComposeBtnWrapper">
        <button
          type="button"
          onClick={event => {
            this.props.handleCreate(true);
          }}
        >
          <IntlMessages id="product.create" />
        </button>
        <button
          type="button"
          onClick={event => {
            this.props.handleEdit(true);
          }}
        >
          <IntlMessages id="product.edit" />
        </button>
      </ProductComposeBtnWrapper>
    );
  }
}
