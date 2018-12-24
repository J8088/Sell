import React, { Component } from 'react';
import ProductPagination from './productPagination.style';
import { rtl } from '../../settings/withDirection';

export default class extends Component {
  render() {
    return (
      <ProductPagination className="isoMailPagination">
        <button type="button" className="prevPage">
          <i
            className={
              rtl === 'rtl' ? 'ion-ios-arrow-forward' : 'ion-ios-arrow-back'
            }
          />
        </button>

        <button type="button" className="nextPage">
          <i
            className={
              rtl === 'rtl' ? 'ion-ios-arrow-back' : 'ion-ios-arrow-forward'
            }
          />
        </button>
      </ProductPagination>
    );
  }
}
