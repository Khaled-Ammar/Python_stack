var cart=document.getElementById("count").innerText;
var counter=parseInt(cart);
var countElement = document.querySelector("#count");
console.log(countElement);
function add1() {
    counter++
    countElement.innerText = counter ;
    console.log(counter)
}

////////////////////////

function sort() {
    var value = document.getElementById("sortIt").value;
    document.getElementById("change").innerHTML ="62 Products, sorted by Price &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp";
}