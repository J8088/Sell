import React, {Component} from 'react';
import {connect} from 'react-redux';
import Scrollbars from '../../components/customScrollBar.js';
import {InputSearch} from '../../components/uielements/input';
import productsList from '../../components/products/productsList';
import productsBuckets from '../../components/products/productsBuckets';
import productsTags from '../../components/products/productsTags';
import singleProduct from '../../components/products/singleProduct';
import ComposeBtn from '../../components/products/productComposeBtn';
import EditThing from '../../components/products/editThing';
import actions from '../../redux/products/actions';
import PaginationControl from '../../components/products/productPagination';
import IntlMessages from '../../components/intlMessages';
import mailSelector from '../../redux/products/selector';
import Products from './products.style';

const {
  fetchProducts,
  fetchProduct,
  saveThing,
  fetchCategories,
  fetchFilters,
  update,
  filterAction,
  selectProduct,
  createThing,
  editThing,
  changeReplyMail,
  changeSearchString,
} = actions;

class DesktopView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      search: this.props.searchString,
    };
  }

  componentDidMount() {
    this.props.fetchProducts();
    //TODO Convert categories in product from [{},{}...] to [...]
    this.props.fetchCategories();
    this.props.fetchFilters();
  }


  onInputChange = (target) => {
    const {thing} = Object.assign({}, this.props);
    const {name, value, checked} = target;

    if (name) thing[name] = value;

    this.props.update(thing);
  };

  onSave = () => {
    this.props.saveThing(this.props.thing);
  };

  onFiltersCheckBoxChange = (target) => {
    const {value, checked} = target;
    const {thing, filters} = Object.assign({}, this.props);
    const filter = filters.find((f) => {
      return f.filter_id === value
    });

    if (checked) {
      thing.filters.push(filter);
    } else {
      const index = thing.filters.indexOf(filter);
      thing.filters.splice(index, 1);
    }

    this.props.update(thing);
  };

  onCategoriesCheckBoxChange = (target) => {
    const {value, checked} = target;
    const {thing, categories} = Object.assign({}, this.props);
    const category = categories.find((cat) => {
      return cat.category_id === value
    });

    if (checked) {
      thing.categories.push(category);
    } else {
      const index = thing.categories.indexOf(category);
      thing.categories.splice(index, 1);
    }

    this.props.update(thing);
  };

  onImageChange = (info) => {
    const {fileList, file} = info;
    const {thing} = Object.assign({}, this.props);

    if (file.status === 'removed') {
      const headers = new Headers();
      headers.append("Content-Type", "application/json");
      headers.append('Accept', 'application/json');

      fetch('http://localhost:8000/api/image/', {
        method: 'DELETE',
        headers: headers,
        body: JSON.stringify({"product_image_id": (file.response && file.response.product_image_id) || file.uid})
      }).then(response => {

        thing.product_images = thing.product_images
          .filter((i) => {
          return i.product_image_id !== ((file.response && file.response.product_image_id) || file.uid);
        });

        thing.diffFileList = fileList;
        this.props.update(thing);

        return response.json();
      })
    }

    if (file.status === "uploading") {
      const {thing} = Object.assign({}, this.props);
      thing.diffFileList = fileList;
    }

    if(file.status === "done"){
      const {thing} = Object.assign({}, this.props);
      thing.product_images.push(file.response);
    }

    this.props.update(thing);
  };


  render() {
    const {
      products,
      thing,
      categories,
      filters,
      filterAttr,
      filterProducts,
      editMode,
      replyMail,
      selectMail,
      filterAction,
      createThing,
      editThing,
      changeReplyMail,
      changeSearchString,
    } = this.props;

    const {search} = this.state;

    let singleProductComponent = (
      <p className="isoNoMailMsg" key="noProdMessage">
        <IntlMessages id="email.noMessage"/>
      </p>
    );

    if (thing.product_id) {
      singleProductComponent = singleProduct(
        products,
        filterProducts,
        thing,
        replyMail,
        changeReplyMail,
        selectMail
      );
    }

    return (
      <Products className="isomorphicMailBox">
        <div className="isoLeftWrapper">
          <ComposeBtn
            handleCreate={createThing}
            handleEdit={editThing}/>
          <div className="isoMailOptions">
            <Scrollbars style={{height: this.props.height}}>
              {productsBuckets(products, filterAction, filterAttr)}
              {productsTags(products, filterAction, filterAttr)}
            </Scrollbars>
          </div>
        </div>

        {/* The THINGS LIST */}
        {editMode ? (
          ''
        ) : (
          <div className="isoMiddleWrapper">
            <div className="isoBucketLabel">
              <h3>{filterAttr.bucket}</h3>
              <PaginationControl/>
            </div>
            <div className="isoSearchMailWrapper">
              <InputSearch
                placeholder="Search Product"
                value={search}
                className="isoSearchEmail"
                onChange={event =>
                  this.setState({search: event.target.value})
                }
                onSearch={value => changeSearchString(value)}
              />
            </div>
            <Scrollbars>
              {productsList(products, this.props.fetchProduct, thing)}
            </Scrollbars>
          </div>
        )}

        {/* CREATING THING / EDITING THING */}
        <div className="isoSingleMailWrapper">
          <Scrollbars style={{height: this.props.height}}>
            {
              editMode ? (
                <EditThing
                  thing={thing}
                  handleSaveThing={this.onSave}
                  handleImageChange={this.onImageChange}
                  handleInputChange={this.onInputChange}
                  handleFiltersCheckBoxChange={this.onFiltersCheckBoxChange}
                  handleCategoriesCheckBoxChange={this.onCategoriesCheckBoxChange}
                  categories={categories}
                  filters={filters}/>
              ) : (
                singleProductComponent
              )}
          </Scrollbars>
        </div>
      </Products>
    );
  }
}

function mapStateToProps(state) {
  const {
    products,
    thing,
    categories,
    filters,
    tag,
    selectedMail,
    filterAttr,
    editMode,
    replyMail,
    searchString,
  } = state.Products;
  return {
    products,
    thing,
    categories,
    filters,
    tag,
    selectedMail,
    filterAttr,
    editMode,
    replyMail,
    searchString,
    filterProducts: mailSelector(state.Products),
  };
}

export default connect(mapStateToProps, {
  fetchProducts,
  fetchProduct,
  fetchCategories,
  fetchFilters,
  saveThing,
  update,
  filterAction,
  selectProduct,
  createThing,
  editThing,
  changeReplyMail,
  changeSearchString,
})(DesktopView);
