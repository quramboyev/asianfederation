
const bannerEl = document.getElementById('banner')
const galleryEl = document.getElementById('galleryl')

function swapBanner(el, newImage) {
    el.src = bannerEl.src
    bannerEl.src = newImage
    console.log('swapping')
}

galleryEl.onclick = (event) => {
    const item = event.target
    if (item instanceof HTMLLIElement) {
        swapBanner(item, item.children[0].src)
    }
    if (item instanceof HTMLImageElement) {
        swapBanner(item, item.src)
    }
}


document.getElementById('clickableVid').onclick = () => {
    window.location.href = 'https://h2hfight.tv/'; 
};

document.getElementById('clickableDoping').onclick = () => {
    window.location.href = 'https://www.judo.ru/news/10902'; 
};

// scroll bar
let activeAccount = document.querySelector('.contest-button-item.active')


function filterEvents(type, btn) {
    const events = document.querySelectorAll('.event');
    activeAccount.classList.remove('active');
    activeAccount = btn;
    activeAccount.classList.add('active');
    events.forEach(event => {
        if (type === 'upcoming' && event.classList.contains('upcoming')) {
            event.classList.remove('hidden');
        } else if (type === 'completed' && event.classList.contains('completed')) {
            event.classList.remove('hidden');
        } else {
            event.classList.add('hidden');
        }
    });
}

function showCalendar() {
    alert("Показать календарь - функция не реализована");
}


// slides
const slides = document.querySelector('.slides');
let prevIndex = 0;
let currentIndex = 0;
const totalSlides = slides.children.length;

const keys = {
    right: 'ArrowRight',
    left: 'ArrowLeft'
}

const theme = {
    '--clr-white': ['white', 'black']
}

const moveNext = () => {
    prevIndex = currentIndex;
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlider();
}

const movePrev = () => {
    prevIndex = currentIndex;
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
    updateSlider();
}

document.querySelector('.next').onclick = moveNext;
document.querySelector('.prev').onclick = movePrev;

document.onkeydown = (event) => {
    switch (event.key) {
        case keys.right: {
            moveNext()
            console.log('next')
            break
        }
        case keys.left: {
            movePrev()
            console.log('prev')
            break
        }
    }
}

setInterval(() => {
    prevIndex = currentIndex;
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSlider()
}, 3000)

function updateSlider() {
    
    slides.style.transform = `translateX(-${currentIndex * slides.scrollWidth / totalSlides}px)`;
}