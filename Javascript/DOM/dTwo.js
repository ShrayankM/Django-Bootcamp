var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");

//H1 #one
headOne.addEventListener('mouseover', function(){
    headOne.textContent = "Mouse over me";
});

headOne.addEventListener('mouseout', function(){
    headOne.textContent = "Hover Over Me!";
});

//H1 #Two
headTwo.addEventListener('click', function(){
    headTwo.textContent = "Clicked!";
});
