import actions from './actions';

const initState = {
  products: [],
  thing: {categories: [], filters: [], product_images: []},
  selectedProduct: null,
  categories: [],
  filters: [],
  tag: undefined,
  selectedMail: -1,
  filterAttr: {bucket: 'Products'},
  editMode: false,
  replyMail: false,
  searchString: ''
};

export default function reducer(state = initState, action) {
  switch (action.type) {
    case actions.FETCH_PRODUCTS:
      return {
        ...state,
        loading: true,
        searcText: action.payload.searcText
      };
    case actions.FETCH_PRODUCTS_SUCCESS_RESULT:
      return {
        ...state,
        loading: false,
        error: false,
        products: action.products,
        total_count: action.total_count,
        prevPageToken: action.prevPageToken,
        nextPageToken: action.nextPageToken
      };
    case actions.FETCH_CATEGORIES:
      return {
        ...state,
        loading: true
      };
    case actions.FETCH_CATEGORIES_SUCCESS_RESULT:
      return {
        ...state,
        loading: false,
        error: false,
        categories: action.categories,
        total_count: action.total_count
      };
    case actions.FETCH_FILTERS:
      return {
        ...state,
        loading: true
      };
    case actions.FETCH_FILTERS_SUCCESS_RESULT:
      return {
        ...state,
        loading: false,
        error: false,
        filters: action.filters,
        total_count: action.total_count
      };
    case actions.FETCH_PRODUCT:
      return {
        ...state,
        loading: true,
        productId: action.payload.productId
      };
    case actions.FETCH_PRODUCT_SUCCESS_RESULT:
      return {
        ...state,
        loading: false,
        error: false,
        thing: action.thing,
      };
    case actions.SAVE_THING_SUCCESS_RESULT:
      return {
        ...state,
        loading: false,
        error: false,
        thing: action.thing,
      };
    case actions.FILTER_ATTRIBUTE:
      return {
        ...state,
        editMode: false,
        replyMail: false,
        selectedMail: -1,
        filterAttr: {...action.filterAttr}
      };
    case actions.SELECTED_MAIL:
      return {
        ...state,
        replyMail: false,
        selectedMail: action.selectedMail,
        allMails: action.allMails
      };
    case actions.CREATE_THING:
      return {
        ...state,
        thing: {categories: [], filters: [], product_images: []},
        editMode: action.editMode
      };
    case actions.EDIT_THING:
      return {
        ...state,
        editMode: action.editMode
      };
    case actions.THING_UPDATE:
      return {
        ...state,
        thing: action.payload.data,
      };
    case actions.REPLY_MAIL:
      return {
        ...state,
        replyMail: action.replyMail
      };
    case actions.SEARCH_STRING:
      return {
        ...state,
        searchString: action.searchString
      };
    default:
      return state;
  }
}
