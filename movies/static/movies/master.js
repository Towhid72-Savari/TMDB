var starWidth = 12;

$.fn.stars = function() {
  return $(this).each(function() {
    $(this).html($('<span />').width(Math.max(0, (Math.min(10, parseFloat($(this).html())))) * starWidth));
  });
};
$(document).ready(function() {
  $('span.stars').stars();
});


var swiper = new Swiper('.blog-slider', {
      spaceBetween: 30,
      effect: 'fade',
      loop: true,
      mousewheel: {
        invert: false,
      },
      // autoHeight: true,
      pagination: {
        el: '.blog-slider__pagination',
        clickable: true,
      }
    });