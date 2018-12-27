import React, { Component } from 'react';
import { Popconfirm } from 'antd';
import Button from '../uielements/button';
import notification from '../notification';

export default class extends Component {
  render() {
    const { product, clearProduct } = this.props;
    let name = '';
    if (product.product_name) {
      name = `${product.product_name} `;
    }
    if (product.product_description) {
      name = `${name}${product.product_description}`;
    }
    if (!name) {
      name = 'No Name';
    }
    return (
      <Popconfirm
        title={`Sure to close ${name}?`}
        okText="CLOSE"
        cancelText="No"
        onConfirm={() => {
          notification('error', `${name} Closed`, '');
          clearProduct(product.product_id);
        }}
      >
        <Button icon="close" type="button" className="isoDeleteBtn" />
      </Popconfirm>
    );
  }
}
