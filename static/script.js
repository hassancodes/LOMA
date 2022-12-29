const presentans = document.getElementsByClassName("present-answer")
console.log("lol");
window.onload = ()=>{
    gsap.fromTo(".present-answer", {opacity:0} , {opacity:1,y:"30",delay:0.1, stagger:0.9})
}