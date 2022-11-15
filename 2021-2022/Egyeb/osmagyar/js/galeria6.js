function shufflePictures(list) {
	if (typeof(list) == "string")
		list = document.getElementById(list);

	var elems = list.getElementsByTagName("li");
	for (var steps = 0; steps < 5; steps++) {
		var a = Math.floor(Math.random() * elems.length);
		var b = Math.floor(Math.random() * elems.length);
		
		if (a != b) {
			temp = elems[a].innerHTML;
			elems[a].innerHTML = elems[b].innerHTML;
			elems[b].innerHTML = temp;
		}
	}
}

function initPage() {
	var pins = ["pin_blue", "pin_cyan", "pin_green", "pin_red", "pin_white", "pin_yellow" ];
	
	var spans = document.getElementsByTagName("span");
	for (var s = 0; s < spans.length; s++) {
		var bg = Math.floor(Math.random() * pins.length);
		var dx = Math.floor(Math.random() * 20) - 10;
		var dy = Math.floor(Math.random() * 10) - 5;

		spans[s].style.backgroundImage = "url(images/" + pins[bg] + ".png)";
		spans[s].style.left = spans[s].offsetLeft + dx + "px";
		spans[s].style.top = spans[s].offsetTop + dy + "px";
	}
	
	shufflePictures("photos");
}

window.onload = initPage;