import $ from 'jquery';
import 'bootstrap';
import 'bootstrap/js/dist/util';
import 'bootstrap/js/dist/dropdown';

import 'owl.carousel/dist/assets/owl.carousel.css';
import 'owl.carousel';

import '../../css/main.scss';

window.jQuery = $;
window.$ = $;

$(window).scroll(function () {
  if ($(this).scrollTop() > 55) {
    $('#mainNavBar').addClass('fixed-top');
    $('body').css('padding-top', '55px');
  } else {
    $('#mainNavBar').removeClass('fixed-top');
    $('body').css('padding-top', '0');
  }
});

$(document).ready((e) => {
  homeCarousel();
  productDetailsCarousel();
  homeProductsCarousel();
  homeCategoriesCarousel();
  applyFilterForm();
  applySearchForm();

  function applyFilterForm() {
    const $form = $('form.sidebar-block__form');
    const $inputFields = $form.find('input[type=checkbox]');
    $inputFields.on('change', (e) => {
      $form.submit();
    });
  }

  function applySearchForm() {
    const $form = $('#searchForm');
    const $inputFields = $form.find('input[type=text]');
    $inputFields.on('keyup', (e) => {
      if (e.keyCode === 13) {
        $form.submit();
      }
    });
  }

  function productDetailsCarousel() {
    $('#product-details-images').owlCarousel(
      {
        loop: true,
        margin: 10,
        nav: true,
        items: 1,
        navClass: ['owl-button', 'owl-button owl-next-button']
      }
    ).mouseenter(function () {
      $(".owl-button").fadeIn(600);
    }).mouseleave(function () {
      $(".owl-button").fadeOut(800);
    });
  }

  function homeCarousel() {
    $('#home-carousel').owlCarousel(
      {
        loop: true,
        margin: 10,
        nav: true,
        items: 1,
        autoplay: true,
        autoplayTimeout: 3000,
        responsiveRefreshRate: 1000,
        autoplayHoverPause: true,
        dots: false,
        navClass: ['owl-home-button owl-home-next-button', 'owl-home-button'],
        navText: [
          "<img class='owl-home-button__img'  src='/static/img/angle-right-circle-black.svg'>",
          "<img class='owl-home-button__img' src='/static/img/angle-left-circle-black.svg'>"
        ]
      }
    ).mouseenter(function () {
      $(this).find(".owl-home-button").fadeIn(200);
    }).mouseleave(function () {
      $(this).find(".owl-home-button").fadeOut(200);
    });
  }

  function homeProductsCarousel() {
    $('#home-block')
      .find('.products-grid>div>div>.owl-carousel-products')
      .each(function () {
        $(this).owlCarousel({
          loop: false,
          margin: 5,
          nav: true,
          items: 4,
          autoWidth: false,
          autoplay: false,
          dots: false,
          navClass: ['owl-products-button', 'owl-products-button owl-products-next-button'],
          navText: [
            "<img class='owl-products-button__img' src='/static/img/angle-left-circle-black.svg'>",
            "<img class='owl-products-button__img'  src='/static/img/angle-right-circle-black.svg'>"
          ]
        }).mouseenter(function () {
          $(this).find('.owl-products-button').fadeIn(200);
        }).mouseleave(function () {
          $(this).find('.owl-products-button').fadeOut(200);
        });
      });
  }

  function homeCategoriesCarousel() {
    $('#home-block')
      .find('.products-grid>div>div>.owl-carousel-categories')
      .each(function () {
        $(this).owlCarousel({
          loop: true,
          margin: 5,
          nav: true,
          items: 8,
          autoWidth: false,
          autoplay: false,
          dots: false,
          navClass: ['owl-products-button', 'owl-products-button owl-products-next-button'],
          navText: [
            "<img class='owl-products-button__img' src='/static/img/angle-left-circle-black.svg'>",
            "<img class='owl-products-button__img'  src='/static/img/angle-right-circle-black.svg'>"
          ]
        }).mouseenter(function () {
          $(this).find('.owl-products-button').fadeIn(200);
        }).mouseleave(function () {
          $(this).find('.owl-products-button').fadeOut(200);
        });
      });
  }

});

