function predict(){

let stock=
document.getElementById(
"stock"
).value;

fetch("/predict",{

method:"POST",

headers:{
"Content-Type":
"application/x-www-form-urlencoded"
},

body:"stock="+stock

})

.then(response=>response.json())

.then(data=>{

document.getElementById(
"result"
).innerHTML=

"Predicted Price: $"+
data.prediction

})

}