let colorInput = document.querySelector("input");
let button = document.querySelector("button");
let box = document.querySelector(".box3");

button.addEventListener("click", function(){
    let zawartosc = colorInput.value;
    if(zawartosc){
        box.style.backgroundColor = zawartosc;
    }
    else{
        box.style.backgroundColor = "black";
    }
});