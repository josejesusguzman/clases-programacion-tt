btn_cherk = document.getElementById("btn_cherk");

btn_cherk.addEventListener('click', function(e) {
    const audio = new Audio('cherk.mp3');
    audio.play();
    document.getElementsByClassName("cherk")[0].style.display = 'block';
})