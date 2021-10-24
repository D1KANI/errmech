$(document).ready(function(){
  $('.homepage .slider').slick({
    fade: true,
    speed: 800,
    autoplay: true,
    autoplaySpeed: 5000,
    dots: true,
    draggable: false, 
    responsive: [
      {
        breakpoint: 1140,
        settings: {
          arrows: false,
        }
      },
    ]
  });

  $('.header-burger').click(function() {
    $(this).toggleClass('active');
    $('.menu').slideToggle(400);
  });

  $('#theme').click(function() {
    $(this).find('.theme__checkbox').toggleClass('dark')
  });

  $('.images-small__image-wrapper').click(function() {
    let imgLink = $(this).find('img').attr('src');
    $('.images-big__image').attr('src', imgLink);
  });

  $('.item-switches__item').click(function() {
    if (!$(this).hasClass('disabled')) {
      $('.item-switches__item').removeClass('active');
      $(this).addClass('active');
    }
  });

  $('.checkbox').click(function() {
    $(this).toggleClass('active');
  });
});