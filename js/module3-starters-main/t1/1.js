list = ["First item", "Second item", "Third item"]

for (i = 0; i < list.length; i++){
	document.getElementById("target").innerHTML += "<li>" + list[i] + "</li>"
}

document.getElementById("target").classList.add("my-list")