//console.log(1)

var a = 8
var b = "8"
a = b
console.log(typeof(a))
console.log(typeof(b))
console.log(typeof(c))

var car = {
    color: 'red',
    price: 1000
}
console.log(car.color)
console.log(car.year)

var user = ['a',"b",`c`]
var age = 5
console.log(`age: ${age}`)

var x
function add(y) {
   return x+y
}
// add = (x+y) => x+y
// add = (x+y) => {x+y}

(x<1) ? x++ : x--
