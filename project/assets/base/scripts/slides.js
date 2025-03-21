
// slides
const slides = document.querySelector('.slides');
let prevIndex = 0;
let currentIndex = 0;
const totalSlides = slides.children.length;
const width = slides.parentElement.offsetWidth
slides.style.width = `${width * totalSlides}px`

for (let slide of slides.children)
    slide.style.width = `${width}px`

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
            break
        }
        case keys.left: {
            movePrev()
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
