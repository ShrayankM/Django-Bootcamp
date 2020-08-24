var blocks = document.querySelectorAll("td");
var restart = document.querySelector("#restart");
// console.log(blocks);

restart.addEventListener('click', function(){
    for(var i = 0; i < blocks.length; i++){
        blocks[i].textContent = '';
    }
});

for(var i = 0; i < blocks.length; i++){
    blocks[i].addEventListener('click', function(){
        if(this.textContent === '')
            this.textContent = 'X';
        else if(this.textContent === 'X')
            this.textContent = 'O';
        else
            this.textContent = '';
    });
}
