
const wineNames = document.querySelectorAll(".wineName");
const productAdd = document.getElementById("productAdd");
const srhByName = document.getElementById("srhByName");
const wineList = document.getElementById("wineList");
const btnDeletes = document.querySelectorAll("input[name=btnDelete]")


function deleteRow() {
	const row = this.parentNode;
	row.replaceChildren();
}

function deleteDefaultRow() {
	const row = this.parentNode;
	wineId = row.querySelector("input[name=wineId]").value
	url = "/store/discontinue-product?wineid=" + wineId
	fetch(url).then((response) => response.json()).then((data) => alert(data["result"]))


	row.replaceChildren();
}

function searchByName(){
	const srhKeyWord = this.value;
	const url = "search-product?srhkeyword=" + srhKeyWord
	const xhttp = new XMLHttpRequest();
	
	xhttp.onreadystatechange = () => {
		if (xhttp.readyState === XMLHttpRequest.DONE){
			if(xhttp.status === 200){
				const result = xhttp.response;
				//해야할 행동(리스폰스 값 받아서 html에 div row - div col - innerText로 뿌려주기)
			//	alert(result.result[0]);
				wineList.replaceChildren();
				
				for(let i = 0; i < result.result.length; i++){
					
					console.log(result.result[i][1]);
					
					
					
					const newWineRow = document.createElement("div");
					newWineRow.setAttribute("id", "wineRow" + i);
					newWineRow.setAttribute("class", "row wineRow");
					
					const newWineCol = document.createElement("div");
					newWineCol.setAttribute("id", result.result[i][1]);
					newWineCol.setAttribute("class", "col wineName");
					
					const newWineId = document.createElement("input");
					newWineId.setAttribute("type", "hidden");
					newWineId.setAttribute("id", result.result[i][1] + 1);
					newWineId.setAttribute("value", result.result[i][0]);
					
					const newWineCapacity = document.createElement("input");
					newWineCapacity.setAttribute("type", "hidden");
					newWineCapacity.setAttribute("id", result.result[i][1] + 2);
					newWineCapacity.setAttribute("value", result.result[i][2]);
					
					const newWineAlc = document.createElement("input");
					newWineAlc.setAttribute("type", "hidden");
					newWineAlc.setAttribute("id", result.result[i][1] + 3);
					newWineAlc.setAttribute("value", result.result[i][3]);
					
					wineList.appendChild(newWineRow);
					
					const newListRow = document.getElementById("wineRow" +i);
					newListRow.appendChild(newWineCol);
					
					const newListeCol = document.getElementById(result.result[i][1]);
					newListeCol.innerText = result.result[i][1];
					newListeCol.appendChild(newWineId);
					newListeCol.appendChild(newWineCapacity);
					newListeCol.appendChild(newWineAlc);
				
				}
				const wineNames = document.querySelectorAll(".wineName");
				for(let i = 0; i < wineNames.length; i++){
					wineNames[i].addEventListener("click", addElement); 
					}
			}
			else if (xhttp.status === 500) {
				console.log("서버에 문제가 발생했습니다. 잠시 뒤 다시 시도해주세요");
			}
			else {
				alert("문제가 발생했습니다 잠시 뒤 다시 시도해주세요");
			}
		}
//		else{
//			alert("문제가 발생했습니다 잠시 뒤 다시 시도해주세요 xhttp.readState");
//		}
	};
	
	xhttp.open("GET", url);
	xhttp.responseType = "json";
	xhttp.send();
}





function addElement(){
	const tid = this.id;
	const tid1 = tid + 1;
	const tid2 = tid + 2;
	const tid3 = tid + 3;
	const tid4 = tid + 4;
	const tid5 = tid + 5;
	const tid6 = tid + 6;
	
	if (document.getElementById(tid4)) {
		alert("이미 추가된 상품입니다")
	}
	else{
		
		const wineId = document.getElementById(tid1);
		const wineCapacity = document.getElementById(tid2);
		const wineAlc = document.getElementById(tid3);
		
		const newRow = document.createElement("div");
		newRow.setAttribute("id", tid4);
		newRow.setAttribute("class", "row");
		
		const newCol = document.createElement("div");
		newCol.setAttribute("id", tid5);
		newCol.setAttribute("class", "col");
		
		const newPdtId = document.createElement("input");
		newPdtId.setAttribute("type", "hidden");
		newPdtId.setAttribute("name", "wineId");
		newPdtId.setAttribute("value", wineId.value);
		newPdtId.setAttribute("readonly", "true")
		
		const newPdtName = document.createElement("input");
		newPdtName.setAttribute("type", "text");
		newPdtName.setAttribute("class", "col");
		newPdtName.setAttribute("name", "wineName");
		newPdtName.setAttribute("value", tid);
		newPdtName.setAttribute("readonly", "true")
		
		const newPdtCpcity = document.createElement("input");
		newPdtCpcity.setAttribute("type", "text");
		newPdtCpcity.setAttribute("class", "col-1");
		newPdtCpcity.setAttribute("name", "wineCapacity");
//		newPdtCpcity.setAttribute("style", "width:8%");
		newPdtCpcity.setAttribute("value", wineCapacity.value);
		newPdtCpcity.setAttribute("readonly", "true");
		
		const newPdtAlc = document.createElement("input");
		newPdtAlc.setAttribute("type", "text");
		newPdtAlc.setAttribute("class", "col-1");
		newPdtAlc.setAttribute("name", "wineAlc");
		newPdtAlc.setAttribute("value", wineAlc.value);
//		newPdtAlc.setAttribute("style", "width:8%");
		newPdtAlc.setAttribute("readonly", "true");
		
		const newPdtPrice = document.createElement("input");
		newPdtPrice.setAttribute("type", "text");
		newPdtPrice.setAttribute("class", "col-1");
		newPdtPrice.setAttribute("name", "sellPrice");
		newPdtPrice.setAttribute("maxlength", "5")
		
		const newPdtPromot = document.createElement("input");
		newPdtPromot.setAttribute("type", "text");
		newPdtPromot.setAttribute("class", "col");
		newPdtPromot.setAttribute("name", "sellPromot");
		
		
		const newDelBtn = document.createElement("input");
		newDelBtn.setAttribute("type", "button");
		newDelBtn.setAttribute("id", tid6)
		newDelBtn.setAttribute("class", "col-1");
		newDelBtn.setAttribute("value", "삭제");
		
		productAdd.appendChild(newRow);
//		document.getElementById(tid4).appendChild(newCol);
		document.getElementById(tid4).appendChild(newPdtId);
		document.getElementById(tid4).appendChild(newPdtName);
		document.getElementById(tid4).appendChild(newPdtCpcity);
		document.getElementById(tid4).appendChild(newPdtAlc);
		document.getElementById(tid4).appendChild(newPdtPrice);
		document.getElementById(tid4).appendChild(newPdtPromot);
		document.getElementById(tid4).appendChild(newDelBtn);
		
		document.getElementById(tid6).addEventListener("click", deleteRow);
	}
}

for (var i = 0; i < btnDeletes.length; i++) {
	btnDeletes[i].addEventListener("click", deleteDefaultRow)
}

for (var i = 0; i < wineNames.length; i++) {
	wineNames[i].addEventListener("click", addElement);
}


srhByName.addEventListener("keyup", searchByName)

