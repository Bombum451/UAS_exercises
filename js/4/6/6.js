let target = document.getElementById("target")

let obj = document.getElementById("button")

obj.onclick = function() {query()}

async function query(){
	console.log("yeasd")
	event.preventDefault()
	input = document.getElementById("query").value
	
	fetchstring = "https://api.chucknorris.io/jokes/search?query=" + input
	
	try {
		response = await fetch(fetchstring)
		response = await response.json()
		
	} catch(error) {
		console.log(error.message)
	}
	
	target.innerHTML = ""
	
	for (i = 0; i < response.result.length; i++){
		console.log("wowie")
		let joke = document.createElement("article")
		
		let joketext = document.createElement("p")
		joketext.innerHTML = response.result[i].value
		
		joke.appendChild(joketext)
		target.appendChild(joke)
	}
	
}