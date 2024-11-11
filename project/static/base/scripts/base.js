
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