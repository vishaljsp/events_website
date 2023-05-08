// card show hedie 
let chbtn=document.getElementById("accne")
let removediv=document.getElementById("userhere")
let showdiv=document.getElementById("afteuser")

// price hendling js  id

let btplus=document.getElementById("price_n")
let bt_d=document.getElementById("d_price")
let datashowinput=document.getElementById("show_price")
let cont_price=1;

chbtn.addEventListener("click",() => {
    removediv.remove()
    showdiv.style.display="block";
})


// price hendling js  id
// let np=0;
btplus.addEventListener("click",() => {
    let p=cont_price++
    if(p==4){
        alert("soryy sir you can't take")
    }
    else{
        datashowinput.value=p
    }
    

})

bt_d.addEventListener("click",() => {
    let d=cont_price--
    if(d==0){
        cont_price=0
        alert("max quantty is 1")

    }
    else{
        datashowinput.value=d
    }
    
})