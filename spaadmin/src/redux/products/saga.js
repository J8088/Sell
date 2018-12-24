import {all, takeEvery, put, fork, call} from 'redux-saga/effects';
import actions from './actions';

export const per_page = 10;
const maxResults = 10;
const requestURL = `http://localhost:8000/api/`;

const onFetchReqeust = async (requestParams) =>
  await fetch(
    `${requestURL}${requestParams}`
  )
    .then(res => res.json())
    .then(res => res)
    .catch(error => error);

const onSaveReqeust = async (params) =>
  await fetch(
    `${requestURL}${params.path}/0/`, {
      method: params.method,
      headers: params.headers,
      body: params.body
    }
  )
    .then(res => res.json())
    .then(res => res)
    .catch(error => error);

export function* fetchProducts({payload}) {
  const {searcText} = payload;
  try {
    const searchResult = yield call(
      onFetchReqeust,
      'products/'
    );

    if (searchResult.items) {
      yield put(
        actions.fetchProductsSuccess(
          searchResult.items,
          searchResult.totalResults,
          searchResult.nextPageToken,
          searchResult.prevPageToken
        )
      );
    } else {
      yield put(actions.fetchProductsSuccess());
    }
  } catch (error) {
    yield put(actions.fetchProductsError());
  }
}

export function* fetchCategories({payload}) {
  const {searcText} = payload;
  try {
    const fetchResult = yield call(
      onFetchReqeust,
      'categories/'
    );

    if (fetchResult.items) {
      yield put(
        actions.fetchCategoriesSuccess(
          fetchResult.items,
          fetchResult.totalResults
        )
      );
    } else {
      yield put(actions.fetchCategoriesSuccess());
    }
  } catch (error) {
    yield put(actions.fetchCategoriesError());
  }
}

export function* fetchFilters({payload}) {
  const {searcText} = payload;
  try {
    const fetchResult = yield call(
      onFetchReqeust,
      'filters/'
    );

    if (fetchResult.items) {
      yield put(
        actions.fetchFiltersSuccess(
          fetchResult.items,
          fetchResult.totalResults
        )
      );
    } else {
      yield put(actions.fetchFiltersSuccess());
    }
  } catch (error) {
    yield put(actions.fetchFiltersError());
  }
}

export function* fetchSingleProduct({payload}) {
  const {productId} = payload;

  try {
    const requestRequest = yield call(
      onFetchReqeust,
      `product/${productId}/`
    );

    if (requestRequest) {
      yield put(actions.fetchProductSuccess(requestRequest));
    } else {
      yield put(actions.fetchProductSuccess(requestRequest));
    }
  } catch (error){
    yield put(actions.fetchProductError());
  }
}

export function* saveThing({payload}) {
  // const {thing} = payload;
  const headers = new Headers();

  headers.append("Content-Type", "application/json");
  headers.append('Accept', 'application/json');

  try {
    const params = {
      path: 'product',
      method: 'POST',
      headers: headers,
      body: JSON.stringify(payload)
    };

    const requestResult = yield call(
      onSaveReqeust,
      params
    );

    if (requestResult) {
      yield put(actions.saveThingSuccess(requestResult));
    } else {
      yield put(actions.saveThingSuccess(requestResult));
    }
  } catch (error){
    yield put(actions.saveThingError());
  }
}

export function* filterAction() {
  yield takeEvery(actions.FILTER_ATTRIBUTE, function* () {
  });
}

export default function* rootSaga() {
  yield all([
    fork(filterAction),
    takeEvery(actions.FETCH_PRODUCTS, fetchProducts),
    takeEvery(actions.FETCH_PRODUCT, fetchSingleProduct),
    takeEvery(actions.SAVE_THING, saveThing),
    takeEvery(actions.FETCH_CATEGORIES, fetchCategories),
    takeEvery(actions.FETCH_FILTERS, fetchFilters)
  ]);
}
