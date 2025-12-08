let target = document.getElementById("target")

let obj = document.getElementById("button")

obj.onclick = function() {query()}

async function query(){
	event.preventDefault()
	input = document.getElementById("query").value
	
	try {
		response = await fetch("https://api.tvmaze.com/search/shows?q=$" + input)
		response = await response.json()
		
	} catch(error) {
		console.log(error.message)
	}
	
	target.innerHTML = ""
	
	for (i = 0; i < response.length; i++){
		let show = document.createElement("article")
		
		let title = document.createElement("h2")
		title.innerHTML = response[i]["show"]["name"]
		
		let url = document.createElement("a")
		url.innerHTML = "<br>" + response[i]["show"]["url"]
		url.setAttribute("target", "_blank")
		
		let medimg = document.createElement("img")
		medimg?.setAttribute("src", response[i]["show"]["image"].medium)
		medimg.setAttribute = ("alt", response[i]["show"]["name"])
		
		let summary = document.createElement("div")
		summary.innerHTML = response[i]["show"]["summary"]
		
		show.appendChild(title)
		show.appendChild(medimg)
		show.appendChild(url)
		show.appendChild(summary)
		
		target.appendChild(show)
	}
	
}