// Toggle navbar
function init() {
    const toggleButton = document.querySelector('.navbar .mobile-menu-toggle');
    // console.log(toggleButton);
    const mobileMenu = document.querySelector('.navbar .mobile-menu-items');
    // console.log(mobileMenu);

    toggleButton.addEventListener('click',function () {
        mobileMenu.classList.toggle('active');
    })

}

document.addEventListener('DOMContentLoaded', init);

//change navbar background on scroll
document.addEventListener('scroll',function () {
    const navbar = document.querySelector('.navbar');
    // console.log(navbar);
    if (window.scrollY > 0) {
        navbar.classList.add('navbar-scroll');
    } else {
        navbar.classList.remove('navbar-scroll');
    }
})










