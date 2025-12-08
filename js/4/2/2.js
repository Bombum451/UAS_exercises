let obj = document.getElementById("button")

obj.onclick = function() {query()}

async function query(){
	event.preventDefault()
	input = document.getElementById("query").value
	try {
		response = await fetch("https://api.tvmaze.com/search/shows?q=$" + input)
		console.log(await response.json())
		
	} catch(error) {
		console.log(error.message)
	}
}