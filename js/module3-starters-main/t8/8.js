let obj = document.getElementById('start')

obj.onclick = function() {calc()}

function calc(){
	let int1 = parseInt(document.getElementById("num1").value)
	let int2 = parseInt(document.getElementById("num2").value)
	
	let mode = document.getElementById("operation").value
	
	if (mode == "add"){
		document.getElementById("result").innerHTML = int1 + int2
	}
	if (mode == "sub"){
		document.getElementById("result").innerHTML = int1 - int2
	}
	if (mode == "multi"){
		document.getElementById("result").innerHTML = int1 * int2
	}
	if (mode == "div"){
		document.getElementById("result").innerHTML = int1 / int2
	}
}