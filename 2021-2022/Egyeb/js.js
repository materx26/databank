function d(){
	var d = prompt( "Kérek egy számot!");
	if (isFinite(d)){
		if (Math.floor(d)==d){
			if (d % 2 == 0 ){
				document.write(d + " Páros");
			}else{
				document.write(d + " Páratlan");
			}
		}else{
			document.write(d + " Nem egész!!!");
		}
	}
	else{
		document.write(d + " is not a number!");
	}
}

function dd()
{
	var a = prompt("Kérek egy 100-nál nagyobb páros számot!","0");
	if (a % 2 == 0 && a > 100){
		document.write("OK<br>");
	}else{
		document.write("NEM OK<br>");
	}
}

function d18()
{
	var a = prompt("Kérek 2-vel,vagy 7-el osztható 100-nál nagyobb számot","0");
	if ((a % 2 == 0 || a%2 == 7 )&& a > 100){
		document.write("OK<br>");
	}else{
		document.write("NEM OK<br>");
	}
}
function d19()
{
	var a = prompt("Kérek 2-vel,vagy 7-el osztható 100-nál nagyobb számot","0");
	if (!((a % 2 == 0 || a%2 == 7 )&& a > 100)){
		document.write("OK<br>");
	}else{
		document.write("NEM OK<br>");
	}
}
function d20()
{
	for (i=0; i <=20; i++)
	{
		document.write(i,"<br>");
	}
}
function d22()
{
	for (i=20; i >=0; i--)
	{
		document.write(i,"<br>");
	}
}
function d29()
{
	var n=42;
	while (!isFinite(n)) {
	 n = prompt('Kérek egy számot','0');
	}
	document.write('A megadott szám=', n);
}
function d30(){
	var n=42; 
	do { 
	 n = prompt('Kérek egy számot','0');
	} while (!isFinite(n)); 
	document.write('A megadott szám=', n);
}

function negyzet()
{
	var w = prompt("Adja meg a négyzet oldalhosszát!");
	if (Math.floor(w)==w){
		if (w > 10 && w < 20 && w%3==0){
		document.write("Terület: "+ w*w);
		document.write("Kerülete: "+ 4*w);
		}
		else{
			alert("A szám nem nagyobb 10-nél és nem kisseb 20-nál vagy nem osztható 3-mal");
		}
	}else{
		alert("Ez nem egész szám!");
		negyzet();
	}
}