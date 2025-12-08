let target = document.getElementById("target")

async function query(){
	
	try {
		response = await fetch("https://api.chucknorris.io/jokes/random")
		response = await response.json()
		
	} catch(error) {
		console.log(error.message)
	}
	
	target.innerHTML = response.value
	
}

query()