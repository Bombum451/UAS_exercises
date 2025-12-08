let target = document.getElementById("target")

list = ["First item", "Second item", "Third item"]

for (i = 0; i < list.length; i++){
	let bulletpoint = document.createElement('li')
	bulletpoint.innerText = list[i]
	let thing = target.appendChild(bulletpoint)
	thing.classList.add("my-list")
}

target.classList.add("my-list")