$(window).scroll(function () {
  if ($(this).scrollTop() > 50) {
    $('#mainNavBar').addClass('fixed-top');
  } else {
    $('#mainNavBar').removeClass('fixed-top');
  }
});