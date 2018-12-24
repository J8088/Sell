import React from 'react';
import {tags, tagColor} from './productsTags.js';
import ProductListWrapper from './productsList.style';
import {rtl} from '../../settings/withDirection';

export default function productsList(
  products,
  fetchProduct,
  selectedProduct,
  toggleListVisible
) {
  const renderSingleProduct = (product) => {
    const onClick = () => {
      fetchProduct(product.product_id);

      if (toggleListVisible) {
        toggleListVisible();
      }
    };
    const isSelected = selectedProduct.product_id === product.product_id;
    const activeClass = isSelected ? 'activeMail' : '';
    return (
      <div
        key={`list${product.product_id}`}
        onClick={onClick}
        className={`${activeClass} isoMailList`}
      >
        <span
          className="isoLabelIndicator"
        />
        <div className="isoRecipentsImg">
          {product.img ? (
            <img alt="#" src={product.img}/>
          ) : (
            <span>{product.product_id}</span>
          )}
        </div>

        <div className="isoMailInfo">
          <div className="infoHead">
            <p className="isoRecipents">{product.product_name}</p>
            <p className="isoReceiveDate">
              {product.updated_date}
              </p>
            <p className="isoRecipents">
              {product.product_price} {product.product_currency}
              </p>
          </div>
          <p className="isoSubject">{product.product_description}</p>
        </div>
      </div>
    );
  };
  return (
    <ProductListWrapper className="isoMailListWrapper">
      {products.map((product) => renderSingleProduct(product))}
    </ProductListWrapper>
  );
}
