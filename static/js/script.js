$('.navToggle').on('click', function (e) {
  e.preventDefault();
  $('body').toggleClass('navToggleActive');
});

$(window).scroll(function () {
  if ($(this).scrollTop() > 10) {
    $('body').addClass('fixedHeader');
  } else {
    $('body').removeClass('fixedHeader');
  }
});

var testimonialSwiper = new Swiper('.testimonialSwiper', {
  navigation: {
    nextEl: '.test-swiper-button-next',
    prevEl: '.test-swiper-button-prev',
  },
});

var certificatesSlider = new Swiper('.certificatesSlider', {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.cert-swiper-button-next',
    prevEl: '.cert-swiper-button-prev',
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
  },
});

document.addEventListener('DOMContentLoaded', function () {
  var educationSlider = new Swiper('.educationSlider', {
    slidesPerView: 1,
    spaceBetween: 10,
    navigation: {
      nextEl: '.cert-swiper-button-next',
      prevEl: '.cert-swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
});

document.addEventListener('DOMContentLoaded', function () {
  var accomplishmentsSlider = new Swiper('.accomplishmentsSwiper', {
    slidesPerView: 1,
    spaceBetween: 10,
    navigation: {
      nextEl: '.accompl-swiper-button-next',
      prevEl: '.accompl-swiper-button-prev',
    },
    pagination: {
      el: '.accomplishment-pagination',
      clickable: true,
    },
  });
});


