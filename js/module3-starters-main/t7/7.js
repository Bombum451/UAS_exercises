let obj = document.getElementById("trigger")
let img = document.getElementById("target")

obj.onmouseover = function() {img.setAttribute("src", "img/picB.jpg")}
obj.onmouseout = function() {img.setAttribute("src", "img/picA.jpg")}