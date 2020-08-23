var carInfo = new Object();
carInfo.make = "Honda";
carInfo.year = 2009
carInfo.topspeed = "105 miles"

//OR
var car = {make : "Honda", year : 2010, topspeed : "105 miles"}

console.log(carInfo)

//Objects inside objects
var obj = {a: "Hello String", b:[1, 2, 3], c:{inside:['a', 'b']}}

for (key in obj)
    console.log("KEY:" + key + "," + "VALUE:" + obj[key])

//Object Methods
var simple = {
    times: 0,
    prop: "Hello World!",
    called: function(n){
        times += n;
    },
    myMethod: function(prop){
        this.prop = prop;
        this.called(20);
    }
}

console.log(simple)
simple.myMethod("Modified");
console.log(simple)
