function setColor(e) {
    e.bgColor = document.getElementById('selected').bgColor;
}

function selectColor(e) {
    document.getElementById('selected').bgColor = e.bgColor;
}