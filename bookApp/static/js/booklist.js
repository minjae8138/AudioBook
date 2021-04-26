
const listName = document.querySelector(".list-item")
console.log(listName)

listName.forEach(function(input) {
	input.addEventListener('click', function(e) {
		alert('clicked');
		console.log(e.target)
		console.log(e.target.value)
	});
});


//listName.addEventListener('click', function(e){
//	console.log(e.target)
//    console.log(e.target.value)
//});