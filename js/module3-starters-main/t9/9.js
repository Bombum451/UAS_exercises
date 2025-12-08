let obj = document.getElementById('start')

obj.onclick = function() {calc()}

let response

let int1 = ""
let int2 = ""
let mode = ""
let intnum = 1

function calc(){
	int1 = 0
	int2 = 0
	intnum = 1
	
	response = document.getElementById("calculation").value
	
	for (let i = 0; i < response.length; i++){
		if (isNaN(Number(response[i])) == true){
			mode = response[i]
			intnum++
		}
		if ((isNaN(Number(response[i])) == false) && (intnum == 1)){
			int1 += response[i]
		}
		if ((isNaN(Number(response[i])) == false) && (intnum == 2)){
			int2 += response[i]
		}
	}
	
	int1 = parseInt(int1)
	int2 = parseInt(int2)
	
	if (mode == "+"){
		document.getElementById("result").innerHTML = int1 + int2
	}
	if (mode == "-"){
		document.getElementById("result").innerHTML = int1 - int2
	}
	if (mode == "*"){
		document.getElementById("result").innerHTML = int1 * int2
	}
	if (mode == "/"){
		document.getElementById("result").innerHTML = int1 / int2
	}
}