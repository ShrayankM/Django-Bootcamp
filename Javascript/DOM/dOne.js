var header = document.querySelector("h1")

function randomColor(){
    var str = "0123456789ABCDEF";
    var color = "#";
    for(var i = 0; i < 6; i++)
        color += str[Math.floor(Math.random() * 16)];
    return color;
}

function setColor(){
    header.style.color = randomColor();
}

setInterval("setColor()", 500);
