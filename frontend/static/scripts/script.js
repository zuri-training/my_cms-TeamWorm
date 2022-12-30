const menuItems = document.querySelector('.menu-block');
const navBtn = document.querySelector('#nav-btn');

window.onscroll = ()=>{
    const heading = document.querySelector('header');
    if (window.scrollY > 0){
        heading.style.boxShadow = '0 0 10px';
    } else {
        heading.style.boxShadow = 'none';
    }
}

navBtn.addEventListener('click', () => {
    if (navBtn.getAttribute('alt') === 'show menu') {
            menuItems.style.display = 'block';
        navBtn.setAttribute('alt', 'hide menu');
    } else {
            menuItems.style.display = 'none';
        navBtn.setAttribute('alt', 'show menu');
    }
})