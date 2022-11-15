function ev(){
	var sz_ev = prompt("Hány éves vagy?");
	if (isFinite(sz_ev)){
		var idei_ev = new Date().getFullYear();
		document.write(idei_ev-sz_ev);
	}else{
		alert("Ez nem szám!!");
		ev();
	}
}
ev();