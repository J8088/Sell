const actions = {
  FILTER_ATTRIBUTE: 'FILTER_ATTRIBUTE',
  FETCH_CATEGORIES: 'FETCH_CATEGORIES',
  FETCH_CATEGORIES_SUCCESS_RESULT: 'FETCH_CATEGORIES_SUCCESS_RESULT',
  FETCH_CATEGORIES_ERROR_RESULT: 'FETCH_CATEGORIES_ERROR_RESULT',
  FETCH_FILTERS: 'FETCH_FILTERS',
  FETCH_FILTERS_SUCCESS_RESULT: 'FETCH_FILTERS_SUCCESS_RESULT',
  FETCH_FILTERS_ERROR_RESULT: 'FETCH_FILTERS_ERROR_RESULT',
  FETCH_PRODUCTS: 'FETCH_PRODUCTS',
  FETCH_PRODUCTS_SUCCESS_RESULT: 'FETCH_PRODUCTS_SUCCESS_RESULT',
  FETCH_PRODUCTS_ERROR_RESULT: 'FETCH_PRODUCTS_ERROR_RESULT',
  FETCH_PRODUCT: 'FETCH_PRODUCT',
  FETCH_PRODUCT_SUCCESS_RESULT: 'FETCH_PRODUCT_SUCCESS_RESULT',
  SAVE_THING: 'SAVE_THING',
  SAVE_THING_SUCCESS_RESULT: 'SAVE_THING_SUCCESS_RESULT',
  SAVE_THING_ERROR_RESULT: 'SAVE_THING_ERROR_RESULT',
  FETCH_PRODUCT_ERROR_RESULT: 'FETCH_PRODUCT_ERROR_RESULT',
  SELECTED_MAIL: 'SELECTED_MAIL',
  SELECTED_PRODUCT: 'SELECTED_PRODUCT',
  THING_UPDATE: 'THING_UPDATE',
  CREATE_THING: 'CREATE_THING',
  EDIT_THING: 'EDIT_THING',
  REPLY_MAIL: 'REPLY_MAIL',
  SEARCH_STRING: 'SEARCH_STRING',
  fetchProducts: searcText => {
    return ({
      type: actions.FETCH_PRODUCTS,
      payload: {searcText}
    })
  },
  fetchProductsSuccess: (
    products,
    total_count,
    nextPageToken,
    prevPageToken
  ) => ({
    type: actions.FETCH_PRODUCTS_SUCCESS_RESULT,
    products,
    total_count,
    nextPageToken,
    prevPageToken
  }),
  fetchProduct: productId => {
    return ({
      type: actions.FETCH_PRODUCT,
      payload: {productId}
    })
  },
  fetchProductSuccess: (
    thing
  ) => ({
    type: actions.FETCH_PRODUCT_SUCCESS_RESULT,
    thing
  }),
  saveThing: (thing) => {
    return ({
      type: actions.SAVE_THING,
      payload: thing
    });
  },
  saveThingSuccess: (thing) => {
    return ({
      type: actions.SAVE_THING_SUCCESS_RESULT,
      thing
    });
  },
  saveThingError: () => ({
    type: actions.SAVE_THING_ERROR_RESULT,
  }),
  fetchCategories: searcText => {
    return ({
      type: actions.FETCH_CATEGORIES,
      payload: {searcText}
    })
  },
  fetchCategoriesSuccess: (
    categories,
    total_count
  ) => ({
    type: actions.FETCH_CATEGORIES_SUCCESS_RESULT,
    categories,
    total_count
  }),
  fetchFilters: searcText => {
    return ({
      type: actions.FETCH_FILTERS,
      payload: {searcText}
    })
  },
  fetchFiltersSuccess: (
    filters,
    total_count
  ) => ({
    type: actions.FETCH_FILTERS_SUCCESS_RESULT,
    filters,
    total_count
  }),
  fetchProductsError: () => ({
    type: actions.FETCH_PRODUCTS_ERROR_RESULT,
  }),
  fetchProductError: () => ({
    type: actions.FETCH_PRODUCT_ERROR_RESULT,
  }),
  fetchCategoriesError: () => ({
    type: actions.FETCH_CATEGORIES_ERROR_RESULT,
  }),
  fetchFiltersError: () => ({
    type: actions.FETCH_FILTERS_ERROR_RESULT,
  }),
  filterAction: newFilterAttr => {
    return (dispatch, getState) => {
      dispatch({
        type: actions.FILTER_ATTRIBUTE,
        filterAttr: newFilterAttr
      });
    };
  },
  selectProduct: selectedProduct => {
    return (dispatch, getState) => {
      const allProducts = getState().Products.result;
      allProducts[
        allProducts.findIndex(product => product.id === selectedProduct)
        ].read = true;
      dispatch({
        type: actions.SELECTED_PRODUCT,
        selectedProduct,
        allProducts
      });
    };
  },
  createThing: (editMode) => ({
    type: actions.CREATE_THING,
    editMode
  }),
  editThing: editMode => ({
    type: actions.EDIT_THING,
    editMode
  }),
  update: data => ({
    type: actions.THING_UPDATE,
    payload: { data },
  }),
  changeReplyMail: replyMail => ({
    type: actions.REPLY_MAIL,
    replyMail
  }),
  changeSearchString: searchString => ({
    type: actions.SEARCH_STRING,
    searchString
  })
};
export default actions;
