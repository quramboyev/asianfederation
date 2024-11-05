window.onscroll = function() {
    const scrollBtn = document.getElementById("scrollUpBtn");
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollBtn.classList.add("show");
    } else {
        scrollBtn.classList.remove("show");
    }
};

document.getElementById("scrollUpBtn").onclick = function() {
    window.scrollTo({ top: 0, behavior: "smooth" });
};

document.addEventListener("DOMContentLoaded", function() {
        const toggleButton = document.querySelector(".nav-toggle");
        const mobileNav = document.querySelector(".nav-mobile");

        toggleButton.addEventListener("click", function() {
            mobileNav.classList.toggle("show");
        });
    });

$('.slider').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: false,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });