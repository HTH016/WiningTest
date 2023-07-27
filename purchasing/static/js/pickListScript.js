const btnDeletes = document.querySelectorAll("input[name=btnDelete]");

for (var i = 0; i < btnDeletes.length; i++){
	btnDeletes[i].addEventListener("click", deleteElement);
}

function deleteElement(){
	const delCheck = confirm("해당 상품을 장바구니에서 삭제하시겠습니까?");
	
	if (delCheck == true){
		const row = this.parentNode.parentNode;
		const cartDetailId = this.id;
		let purchasePrice = parseInt(document.getElementById("2id" + cartDetailId).innerText.slice(0, -2));
		let allPriceValue = document.getElementById("allPrice").innerText;
		let allPrice = parseInt(allPriceValue.slice(0, -2));
	
	
		const url = "/purchasing/cart-list";
		const myInit = {
			method: "POST",
			headers: {
				"X-CSRFToken": getCookie("csrftoken"),
				"Content-Type":"application/json"
			},
			body: JSON.stringify({
				cartDetailId: cartDetailId,
			}),
		};
		
		fetch(url, myInit)
			.then((response)=>response.json())
			.then((data)=>alert(data["result"]))
	
		row.remove();
		console.log(allPrice - purchasePrice);
		document.getElementById("allPrice").innerText = (allPrice - purchasePrice) + " 원";
	}
	else{
		return false;
	}
	
}

// 주어진 이름의 쿠키를 반환하는데,
// 조건에 맞는 쿠키가 없다면 undefined를 반환합니다.
function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}