let obj = document.querySelector('input[type="submit"]')

obj.onclick = function() {naming()}

let name1 = ""
let name2 = ""

function naming(){
	event.preventDefault()
	console.log("thing")
	name1 = document.querySelector('[name="firstname"]').value
	name2 = document.querySelector('[name="lastname"]').value
	document.getElementById("target").innerText = "Your name is " + name1 + " " + name2
}