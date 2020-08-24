var players = $('.playerInfo');
var color = {
    'background-color' : 'blue'
}
var flag = true;

var countL = []
var arrId = ['#1', '#2', '#3', '#4', '#5', '#6', '#7'];
var arrClass = ['.C1', '.C2', '.C3', '.C4', '.C5', '.C6', '.C7']
var matrix = []

p1 = prompt("Enter your name Player 1, you will be BLUE");
p2 = prompt("Enter your name Player 2, you will be RED");

init();

function init(){
    for(var i = 0; i < 7; i++)
        matrix[i] = new Array(7);

    for(var i = 0; i < 7; i++)
        for(var j = 0; j < 8; j++)
            matrix[i][j] = -1;

    for(var j = 0; j < arrClass.length; j++)
        countL.push( $(arrClass[j]).length );
}

//Toggle For Button CLick
players.text(p1 + " it is your turn");
players.css(color);

function playerChange(){
    if(flag){
        color['background-color'] = 'red';
        players.text(p2 + " it is your turn");
        players.css(color);
        flag = false;
    }
    else{
        color['background-color'] = 'blue';
        players.text(p1 + " it is your turn");
        players.css(color);
        flag = true;
    }
}

function f(arg){
    if(countL[arg] > 0){
        countL[arg] = countL[arg]  - 1;
        $(arrClass[arg]).eq(countL[arg]).css(color);
    }
    else
        return;
}

//BLUE 1, RED 0
function setColor(r, c){
    if(flag)
        matrix[r][c] = 1;
    else
        matrix[r][c] = 0;
}

function checkWon(f){
    if(f)
        return 1;
    return 2;
}

function hCheck(r, c){
    if((c + 3 > 6) && (c - 3 < 0))
        return false;
    var ct;
    if(c + 3 <= 6){
        ct = 1;
        for(var i = c; i < c + 3; i++){
            if(matrix[r][i] !== matrix[r][i + 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    if(c - 3 >= 0){
        ct = 1;
        for(var i = c; i > c - 3; i--){
            if(matrix[r][i] !== matrix[r][i - 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    return false;
}

function vCheck(r, c){
    if((r + 3 > 5) && (r - 3 < 0))
        return false;
    var ct;
    if(r + 3 <= 5){
        ct = 1;
        for(var i = r; i < r + 3; i++){
            if(matrix[i][c] !== matrix[i + 1][c])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    if(r - 3 >= 0){
        ct = 1;
        for(var i = r; (i > 0 && i > r - 3); i--){
            if(matrix[i][c] !== matrix[i - 1][c])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    return false;
}

function dCheck(r, c){
    if(r - 3 < 0 && r + 3 > 5 && c - 3 < 0 && c + 3 > 6)
        return false;
    var ct;
    if(r + 3 <= 5 && c - 3 >= 0){
        ct = 1;
        for(var i = r, j = c; (i < r + 3) && (j > c - 3); i++, j--){
            if(matrix[i][j] !== matrix[i + 1][j - 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    if(r + 3 <= 5 && c + 3 <= 6){
        ct = 1;
        for(var i = r, j = c; (i < r + 3) && (j < c + 3); i++, j++){
            if(matrix[i][j] !== matrix[i + 1][j + 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    if(r - 3 >= 0 && c - 3 >= 0){
        ct = 1;
        for(var i = r, j = c; (i > r - 3) && (j > c - 3); i--, j--){
            if(matrix[i][j] !== matrix[i - 1][j - 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    if(r - 3 >= 0 && c + 3 <= 6){
        ct = 1;
        for(var i = r, j = c; (i > r - 3) && (j < c + 3); i--, j++){
            if(matrix[i][j] !== matrix[i - 1][j + 1])
                break;
            else
                ct++;
        }
    }
    if(ct === 4)
        return true;
    return false;
}

var checkFlag = false;
var p;

function displayFinal(){
    var obj = {
        fontSize: '20px',
        border: '2px solid black',
        color: 'white'
    };
    if(p == 1)
        obj['background-color'] = 'blue';
    else
        obj['background-color'] = 'red';


    $('.playerInfo').fadeOut('fast');
    $('.won').text("Player " + p + " has WON").css(obj);
    // $('.won').css('background', obj);


}


for(var j = 0; j < arrId.length; j++){
    $(arrId[j]).on('click', function(){
        var temp = $(this).attr('id') - 1;
        f($(this).attr('id') - 1);
        var col = temp;
        var row = countL[temp];
        console.log(row + " " + col);
        setColor(row, col);
        if(hCheck(row, col) || vCheck(row, col) || dCheck(row, col)){
            checkFlag = true;
            p = checkWon(flag);
            displayFinal();
        }
        playerChange();
    })
}
