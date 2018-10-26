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
  if ($(this).scrollTop() > 65) {
    $('#mainNavBar').addClass('fixed-top');
  } else {
    $('#mainNavBar').removeClass('fixed-top');
  }
});

$(document).ready((e) => {
  const $form = $('form.sidebar-block__form');
  const $countryFields = $form.find('input[type=checkbox]');
  $countryFields.on('change', (e) => {
    $form.submit();
  });
});

$(document).ready(function () {
  $('.owl-carousel').owlCarousel(
    {
      loop: true,
      margin: 10,
      nav: true,
      items: 1,
      navClass: ['owl-prev-button', 'owl-next-button']
    }
  ).mouseenter(function () {
    $(".owl-next-button").fadeIn(600);
    $(".owl-prev-button").fadeIn(600);
  }).mouseleave(function () {
    $(".owl-next-button").fadeOut(800);
    $(".owl-prev-button").fadeOut(800);
  });
});

