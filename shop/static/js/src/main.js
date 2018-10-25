import $ from 'jquery';
import 'bootstrap';
import 'bootstrap/js/dist/util';
import 'bootstrap/js/dist/dropdown';
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

