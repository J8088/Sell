import React, {Component} from 'react';
import {Icon, Checkbox, Row, Col, Modal} from 'antd';
import Input, {Textarea} from '../uielements/input';
import {Upload} from 'antd';
import {EditProductWrapper} from './editView.style';
import './upload.css';


export default class extends Component {
  constructor(props) {
    super(props);
    this.state = {
      previewVisible: false,
      previewImage: '',
      fileList: []
    };
  }

  handleCancel = () => this.setState({previewVisible: false});

  handlePreview = (file) => {
    this.setState({
      previewImage: file.url || file.thumbUrl,
      previewVisible: true,
    });
  };

  handleChange = (info) => {
    const {fileList, file} = info;
    this.setState((state, props) => {
      return {fileList: fileList};
    });

    if (file.status === 'removed') {
      const headers = new Headers();

      headers.append("Content-Type", "application/json");
      headers.append('Accept', 'application/json');

      fetch('http://localhost:8000/api/image/', {
        method: 'DELETE',
        headers: headers,
        body: JSON.stringify({"image_id": file.response.image_id})
      }).then(response => response.json())
    }
  };

  upload = (data) => {
    const {diffFileList, fileList, handlePreview, handleImageChange, action} = data;
    return diffFileList ? (<Upload
      listType="picture-card"
      defaultFileList={fileList}
      fileList={diffFileList}
      multiple={true}
      onPreview={handlePreview}
      onChange={handleImageChange}
      action={action}
    >
      <div>
        <Icon type="plus"/>
        <div className="ant-upload-text">Upload</div>
      </div>
    </Upload>) : (
      <Upload
        listType="picture-card"
        defaultFileList={fileList}
        multiple={true}
        onPreview={this.handlePreview}
        onChange={handleImageChange}
        action={action}
      >
        <div>
          <Icon type="plus"/>
          <div className="ant-upload-text">Upload</div>
        </div>
      </Upload>
    );
  };

  render() {
    const {product, categories, filters, handleCategoriesCheckBoxChange, handleFiltersCheckBoxChange, handleInputChange, handleImageChange} = this.props;
    const {previewVisible, previewImage} = this.state;

    const fileList = product.product_images.map((p) => {
      return {
        uid: p.uid || p.product_image_id,
        name: p.name || p.product_image_id,
        status: p.status || 'done',
        url: p.product_photo
      };
    });

    return (
      <EditProductWrapper className="isoContactCard">
        <div className="isoContactCardHead">
          <div className="isoPersonImage">
            {this.upload({
              fileList,
              diffFileList: product.diffFileList,
              handlePreview: this.handlePreview,
              handleImageChange,
              action: "//localhost:8000/api/image/"
            })}
            <Modal visible={previewVisible} footer={null} onCancel={this.handleCancel}>
              <img alt="example" style={{width: '100%'}} src={previewImage}/>
            </Modal>
          </div>
        </div>
        <div className="isoContactInfoWrapper">

          <div className="isoContactCardInfos" key="prodId0">
            <p className="isoInfoLabel">Номер</p>
            <p className="isoInfoDetails">{product.product_id || -1}</p>
          </div>

          <div className="isoContactCardInfos" key="prodName0">
            <p className="isoInfoLabel">Назва</p>
            <Input
              placeholder="Назва"
              name="product_name"
              value={product.product_name}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="proddescription0">
            <p className="isoInfoLabel">Опис</p>
            <Textarea
              placeholder="Опис"
              name="product_description"
              value={product.product_description}
              type="textarea"
              rows={3}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodPrice0">
            <p className="isoInfoLabel">Ціна</p>
            <Input
              placeholder="Ціна"
              name="product_price"
              value={product.product_price}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodCurrency0">
            <p className="isoInfoLabel">Валюта</p>
            <Input
              placeholder="Валюта"
              name="product_currency"
              value={product.product_currency}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodslug0">
            <p className="isoInfoLabel">Артикул</p>
            <Input
              placeholder="Артикул"
              name="product_slug"
              value={product.product_slug}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodState0">
            <p className="isoInfoLabel">Статус</p>
            <Input
              placeholder="Статус"
              name="product_state"
              value={product.product_state}
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodSeo0">
            <p className="isoInfoLabel">СЕО</p>
            <Input
              value={product.product_seo}
              placeholder="СЕО"
              name="product_seo"
              onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodAvtive0">
            <p className="isoInfoLabel">Активний</p>
            <Checkbox checked={product.active}
                      name="active"
                      value="active"
                      onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodVisible0">
            <p className="isoInfoLabel">Опублікований</p>
            <Checkbox checked={product.visible}
                      name="visible"
                      value="visible"
                      onChange={event => handleInputChange(event)}
            />
          </div>

          <div className="isoContactCardInfos" key="prodCategories">
            <p className="isoInfoLabel">Категорії</p>
            <div
              style={{width: '100%'}}
            >
              <Row>
                {categories.map(category => {
                  const length = category.category_name.length;
                  const span = length < 10 ? 3 :
                    length >= 10 && length < 15 ? 5 :
                      length >= 15 && length < 20 ? 7 :
                        length >= 20 && length <= 25 ? 9 : 10;

                  return (
                    <Col key={`category${category.category_id}`} span={span}>
                      <Checkbox
                        checked={product.categories.some((cat) => cat.category_id === category.category_id)}
                        value={category.category_id}
                        onChange={event => handleCategoriesCheckBoxChange(event)}>
                        {category.category_name}
                      </Checkbox>
                    </Col>);
                })}
              </Row>
            </div>
          </div>

          <div className="isoContactCardInfos" key="prodFilters">
            <p className="isoInfoLabel">Фільтри</p>
            <div
              style={{width: '100%'}}
            >
              <Row>
                {filters.map(filter => {
                  const length = filter.filter_name.length;
                  const span = length < 10 ? 3 :
                    length >= 10 && length < 15 ? 5 :
                      length >= 15 && length < 20 ? 7 :
                        length >= 20 && length <= 25 ? 9 : 10;

                  return (
                    <Col key={`filter${filter.filter_id}`} span={span}>
                      <Checkbox
                        checked={product.filters.some((f) => f.filter_id === filter.filter_id)}
                        value={filter.filter_id}
                        onChange={event => handleFiltersCheckBoxChange(event)}>{filter.filter_name}</Checkbox>
                    </Col>);
                })}
              </Row>
            </div>
          </div>

        </div>
      </EditProductWrapper>
    );
  }
}
