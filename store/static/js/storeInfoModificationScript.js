const storeRegistForm = document.getElementById("storeInfoModificationForm");
let storeAddress = document.getElementById("storeAddress");
let storeName = document.getElementById("storeName");
let storeEmail = document.getElementById("storeEmail");
const emailRegExp = /^[a-z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}$/;
const storeRegNumRegExp = /([0-9]{3})-?([0-9]{2})-?([0-9]{5})/;
	
	
storeRegistForm.addEventListener("submit", (event) => {
	if(! document.getElementById("storeAddress").value){
		document.getElementById("mainAddress").innerText = "매장 주소를 입력해주세요";
		event.preventDefault();
		return false;
	}
	else if(! document.getElementById("detailStoreAddress").value){
		document.getElementById("detailAddress").innerText = "상세 주소를 입력해주세요";
		event.preventDefault();
		return false;
		
	} 
	else if(! document.getElementById("storeName").value){
		document.getElementById("name").innerText = "상호명을 입력해주세요";
		event.preventDefault();
		return false;
		
	} 
	else if(! document.getElementById("storeRegNum").value){
		document.getElementById("regNum").innerText = "사업자 등록번호를 입력해주세요";
		event.preventDefault();
		return false;
		
	} 
	else if(! document.getElementById("storeEmail").value){
		document.getElementById("email").innerText = "업무용 이메일을 입력해주세요";
		event.preventDefault();
		return false;
		
	}

	else if(document.getElementById("emailCheck").value === "-1"){
		alert("이메일 형식을 확인해주세요");
		event.preventDefault();
		return false;
	}
});
//
//이메일 정규 표현식 /^[a-z0-9_+.-]+@([a-z0-9-]+\.)+[a-z0-9]{2,4}$/
// 사업자 등록번호 정규 표현식 /([0-9]{3})-?([0-9]{2})-?([0-9]{5})/

storeAddress.addEventListener("click", () => {
	 new daum.Postcode({
        oncomplete: function(data) {
            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분입니다.
            // 예제를 참고하여 다양한 활용법을 확인해 보세요.
            document.getElementById("storeAddress").value = data.address;
        }
    }).open();
	let text = document.getElementById("mainAddress");
	
	if(text.innerText){
		text.innerText = '';
	}
});
storeName.addEventListener("click", () => {
	let text = document.getElementById("name");
	
	if(text.innerText){
		text.innerText = '';
	}
});
storeRegNum.addEventListener("click", () => {
	let text = document.getElementById("regNum");
	
	if(text.innerText){
		text.innerText = '';
	}
});
storeEmail.addEventListener("click", () => {
	let text = document.getElementById("email");
	
	if(text.innerText){
		text.innerText = '';
	}
});

storeEmail.addEventListener("keyup", () => {
	let emailResult = emailRegExp.test(storeEmail.value)
	
	if(emailResult == true){
		document.getElementById("emailCheck").value = 1;
		document.getElementById("email").innerText = "유효한 형식입니다";
	}
	else{
		document.getElementById("emailCheck").value = -1;
		document.getElementById("email").innerText = "형식에 맞지 않습니다";
	}
});


