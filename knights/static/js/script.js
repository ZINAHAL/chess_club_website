$(document).ready(() => {

    $('.nav-pills a[href="#nav-coaches"]').on('click', (e) => {
        e.preventDefault();
        $('#nav-coaches').removeClass('hideDiv');
    });

    // First slideshow area dealing with amount of slides to show on which screen size
    $('.mentors_slideshow').slick({
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: true,
        mobileFirst: true,
        responsive: [
            {
                breakpoint:1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint:600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint:200,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            }
        ]
    });

    $('.sponsors_slideshow').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        mobileFirst: true,
        responsive: [
            {
                breakpoint:1024,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint:600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            },
            {
                breakpoint:200,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: false
                }
            }
        ]
    });

    var pattern = /[a-z_\-]+/i;
    var selected_page = pattern.exec(window.location.pathname);
    if(!selected_page) {
        $('#' + 'home_a').addClass('active')
    }else {
        $('#' + selected_page[0] + '_a').addClass('active')
    }

    $('.gallery_slideshow').slick({
        cssEase: 'linear',
        speed: 300,
        dots: true,
        fade: true,
        mobileFirst: true,
        responsive: [
            {
                breakpoint:1024,
                settings: {
                    cssEase: 'linear',
                    speed: 300,
                    dots: true,
                    fade: true,
                }
            },
            {
                breakpoint:200,
                settings: {
                    cssEase: 'linear',
                    speed: 300,
                    infinite: false,
                    dots: false
                }
            }
        ]
    });

    $('#back-to-top-button').on('click', () => {
        console.log('its working');
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });


});