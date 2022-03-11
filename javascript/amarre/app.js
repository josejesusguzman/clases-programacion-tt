//sets a random absolute position to a html element; receives the html element 
function moveElmRand(elm){ 
    elm.style.position ='absolute'; 
    elm.style.top = Math.floor(Math.random()*90+5)+'%'; 
    elm.style.left = Math.floor(Math.random()*90+5)+'%'; 
} 
    
//get the buttons
var btn_no = document.querySelector('#btn_no');
var btn_si = document.querySelector('#btn_si');
    
//register to call moveElmRand() on mouseenter event to #btn_no 
btn_no.addEventListener('mouseenter', function(e){ moveElmRand(e.target);}); 
    
//register click to #btn_no 
btn_no.addEventListener('click', function(e){ 
    alert('¿Cómo de que no? 😡')
    location.reload();
});

btn_si.addEventListener('click', function(e){ alert("Sabia que si querías. Te amo, casemonos 💖")
});
