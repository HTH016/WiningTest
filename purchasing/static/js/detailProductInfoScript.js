const qnty = document.getElementById("qnty");
const btnBuy = document.getElementById("btnBuy")
const sellId = document.getElementById("sellId")

qnty.addEventListener("change", priceCalc);
btnBuy.addEventListener("click", buyListLocation);
					
					
function priceCalc(){
	document.getElementById("purchasePrice").value 
		= document.getElementById("qnty").value * document.getElementById("sellPrice").value;
}


function buyListLocation(){
	link = "buy-list?sellid=" + sellId.value + "&qnty=" + document.getElementById("qnty").value;
	location.href = link;
}
