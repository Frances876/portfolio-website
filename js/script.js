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