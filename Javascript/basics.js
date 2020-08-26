//Variables
var a = 12;
var b = 2.5;
var str = "Hello World";     //strings are immutable (cannot be modified)
var t = true;

//Printing to console
console.log(str)


//Alert Box on Html Page (Pop Up)
alert("This is an alert Box!!!");

//Strings
var s = "Hello" + "World";   //connecting strings
console.log(s.lenght);       //gives length of strings

s = "Hello \n start new line";              // \n is newline character
s = "She said, \"Lets go for a ride\" ";    // backslash (\) can be used to escape ""
var c = s[7];                              //normal indexing for strings


//Casting
var n = Number("45")                    //converts string to numbers (also float)
var s = String(34)                      //converts numbers to string

//Operators( === )
3 == "3"     //returns true  (does not check type)
3 === "3"    //returns false (doess type checking)

null == undefined //return true  (WIERD)
NaN == NaN       //returns false (WIERD)

1 == 1 && 2 == 2   //AND
1 == 1 || 2 == 2   //OR
!(1 == 1)          //NOT

//Control Flow
if ( true ){
    //do something
} else if {
    //do something
} else {
    //do something
}

//WHILE LOOPS
while ( true ){
    //do something
}

//FOR LOOPS
for(var i = 0; i < 5; i++)
    //do something 5 times

//HTML interaction
var i = prompt("Get user input using alert!!!");

//Functions
function functionName(){
    console.log("Function called");
}

function add(a, b){
    return a + b;
}
add(3, 4);

function fName(f = "Jack", e = "Sparrow"){
    console.log(f + " " + e);
}
fName();             //call prints "Jack Sparrow"
fName("Robert");     //call prints "Robert Sparrow"


//ARRAYS
var _arr = [1, 2, 3, 4, 5, 6]                       //all Number array
var _marr = ["string", 23, true, 3.4, 6, "str"]    //mixed array
_arr.length                                        //length of array
var p = _arr.pop()                                 //remove last element from array
_arr.push(8)                                       //push element at back

for(var i = 0; i < _arr.lenght; i++){
    console.log(_arr[i]);
}

for (i in _arr){
    console.log(_arr[i]);
}

for (i of _arr){
    console.log(i);
}

_arr.forEach(function(item, index){
    console.log(item, index)
})

var matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

//Objects
var car = new Object()
car.make = "Suzuki"
car.year = 2009
car.topSpeed = "150 miles"
car["milege"] = "23 miles"    // Object Created: {make: "Suzuki", year: 2009, topSpeed: "150 miles", milege: "23 miles"}


var bike = {make: "Ducati", year: 2016, model: "Enduro"};

var tObject = {a: "str", b: [1, 2, 3], c: {_keyOne: "vOne", _keyTwo: "vTwo"}};  //Nested Objects
for (k in tObject){
    console.log("KEY:" + k + ", VALUE:" + tObject[k])
}

//Objects with methods
var Obj = {
    a: 0,
    b: 0,
    add: function(){
        return this.a + this.b;
    },
    init: function(a, b){
        this.a = a;
        this.b = b;
    }
}

Obj.init(3, 4)
console.log(Obj.add())            //prints 7
