'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

let target = document.getElementById("target")

for (let i = 0; i < students.length; i++){
	let bulletpoint = document.createElement("options")
	bulletpoint.innerText = students[i].name
	bulletpoint.setAttribute("value", students[i].id)
	target.appendChild(bulletpoint)
}