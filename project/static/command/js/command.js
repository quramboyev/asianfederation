const dropDowns = document.getElementById('hidden-part-wrapper')
for (let dropDown of dropDowns.children) {
    if (!(dropDown instanceof HTMLDivElement)) continue
    if (dropDown.children.length !== 2) continue
    if (!(dropDown.children[0] instanceof HTMLButtonElement && dropDown.children[1] instanceof HTMLDivElement)) continue
    dropDown.children[0].onclick = () => dropDown.children[1].classList.toggle('closed')
    const children = dropDown.children[1].children
    const openEl = children[children.length-1]
    openEl.onclick = () => dropDown.children[1].classList.toggle('closed')
}