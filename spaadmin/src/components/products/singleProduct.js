import React from 'react';

import {
  SingleProductContent
} from './singleProduct.style';

export default function singleProduct(
  products,
  filterMails,
  product,
) {
  return (
    <SingleProductContent className="sellSingleProductContent">
      <div className="sellSingleProductHead">
        {product.product_images ? product.product_images.map((image, index) => {
          return (
            <div key={`img${index}`} className="sellSingleProductImage">
              <img alt="#" src={image.product_photo}/>
            </div>);
        }) : <div className="sellSingleProductImage">{''}</div>}
      </div>
      <div className="sellSingleProductWrapper">
        <div className="sellSingleProductInfos" key={`prodName${product.product_name}`}>
          <p className="sellSingleProductInfoLabel">Назва:</p>
          <p className="sellSingleProductInfoDetails">{product.product_name}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodId${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Номер:</p>
          <p className="sellSingleProductInfoDetails">{product.product_id}</p>
        </div>
        <div className="sellSingleProductInfos" key={`proddescription${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Опис:</p>
          <p className="sellSingleProductInfoDetails">{product.product_description}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodPrice${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Ціна:</p>
          <p className="sellSingleProductInfoDetails">{product.product_price}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodCurrency${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Валюта:</p>
          <p className="sellSingleProductInfoDetails">{product.product_currency}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodslug${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Артикул:</p>
          <p className="sellSingleProductInfoDetails">{product.product_slug}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodDate${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Дата:</p>
          <p className="sellSingleProductInfoDetails">{product.updated_date}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodState${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Статус:</p>
          <p className="sellSingleProductInfoDetails">{product.product_state}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodSeo${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">СЕО:</p>
          <p className="sellSingleProductInfoDetails">{product.product_seo}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodAvtive${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Активний:</p>
          <p className="sellSingleProductInfoDetails">{product.active}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodVisible${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Опублікований:</p>
          <p className="sellSingleProductInfoDetails">{product.visible}</p>
        </div>
        <div className="sellSingleProductInfos" key={`prodCat${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Категорії:</p>
          <div className="sellSingleProductInfoVertical">
            {product.categories.map((category) => {
              return (<p key={`category${category.category_id}`}
                         className="sellSingleProductInfoDetails">{category.category_name}; </p>)
            })}
          </div>
        </div>
        <div className="sellSingleProductInfos" key={`prodFilters${product.product_id}`}>
          <p className="sellSingleProductInfoLabel">Фільтри:</p>
          <div className="sellSingleProductInfoVertical">
            {product.filters.map((filter) => {
              return (<p key={`filter${filter.filter_id}`}
                         className="sellSingleProductInfoDetails">{filter.filter_name}; </p>)
            })}
          </div>
        </div>
      </div>
    </SingleProductContent>
  );
}
