const btnCancel = document.getElementById("btnCancel");
const btnDelete = document.querySelectorAll("input[name=btnDelete]");
const buyList = document.getElementById("buyList");



for (var i = 0; i < btnDelete.length; i++){
	btnDelete[i].addEventListener("click", deleteElement);
}



function deleteElement(){
	const delCheck = confirm("해당 상품을 결제 목록에서 삭제하시겠습니까?")
	
	if(delCheck == true){
		const row = this.parentNode.parentNode;
		const cartDetailId = row.id;
		let allPrice = parseInt(document.getElementById("allPrice").value);
		document.getElementById("allPrice").value = allPrice - parseInt(row.querySelector("input[name=purchasePrice]").value);

		if(document.getElementById("cartId")){
			console.log("cartId")
			const url = "/purchasing/remove-buy-list";
			const myInit = {
				method : "POST",
				headers : {
					"X-CSRFToken" : getCookie("csrftoken"),
					"Content-Type" : "application/json",
				},
				body : JSON.stringify({
					cartDetailId: cartDetailId,
				}),
			};
			fetch(url, myInit).then((response)=>response.json()).then((data)=>alert(data["result"]))
		}
		row.remove();
	}
	else{
		return false;
	}
}

//function 

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}


btnCancel.addEventListener("click", function(){
	const checkCancel = confirm("결제를 취소하시겠습니까?\n메인 페이지로 이동합니다");
	
	if (checkCancel == true){
		location.href = "store-list";
	}
	else{
		return false;
	}
});

buyList.addEventListener("submit", function (event){
	
	const userPoint = parseInt(document.getElementById("userPoint").value);
	const allPrice = parseInt(document.getElementById("allPrice").value);
	
	if (allPrice > userPoint){
		alert("포인트가 부족합니다");
		event.preventDefault();
		return false;
	}
	else{
		if (this.querySelectorAll("input[name=sellId]").length == 0){
			alert("선택된 상품이 없습니다");
			event.preventDefault();
			return false;
		}
	}
});
