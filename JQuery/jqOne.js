var head = $('h1');
var h1Text = head.text();
var h3Tag = $('h3');
var textBox = $('input').eq(0);
var sButton = $('input').eq(1);

head.mouseover(function(){
    $(this).text("Hovering Over H1 tag");
})

head.mouseout(function(){
    $(this).text(h1Text);
})

// head.dblclick(function(){
//     $(this).toggleClass('turnRed');
// })

// Using ON
head.on('dblclick', function(){
    $(this).toggleClass('turnRed');
})

// textBox.keypress(function(){
//     h3Tag.toggleClass('turnBlue');
// })

textBox.keypress(function(event){
    if(event.which === 13)
        h3Tag.toggleClass('turnRed');
})

sButton.on('click', function(){
    $('.container').fadeOut(3000);
})
