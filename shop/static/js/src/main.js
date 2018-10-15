import $ from 'jquery';
import 'bootstrap';
import 'bootstrap/js/dist/util';
import 'bootstrap/js/dist/dropdown';
import '../../css/main.scss';

window.jQuery = $;
window.$ = $;

$(window).scroll(function () {
  if ($(this).scrollTop() > 50) {
    $('#mainNavBar').addClass('fixed-top');
  } else {
    $('#mainNavBar').removeClass('fixed-top');
  }
});