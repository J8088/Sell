import { all } from 'redux-saga/effects';
import authSagas from './auth/saga';
import productsSagas from './products/saga';

export default function* rootSaga(getState) {
  yield all([
    authSagas(),
    productsSagas()
  ]);
}
