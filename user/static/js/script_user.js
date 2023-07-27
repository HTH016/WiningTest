$(document).ready(
	function() {
		
		var iderror = "아이디를 입력하세요";
		var passwderror = "비밀번호를 입력하세요";
		var repasswderror = "비밀번호가 다릅니다";
		var nameerror = "이름을 입력하세요";
		var telerror = "전화번호를 입력하세요";
		var emailerror = "이메일을 입력하세요";
		var confirmerror = "중복확인을 해주세요";
		var pointerror = "금액을 입력하세요";
		var ratingerror = "평점을 입력하세요";
		var reviewerror = "내용을 작성하세요";
		
		var inputerror = "회원가입에 실패했습니다 \n 잠시 후 다시 시도하세요";
		var idxerror = "입력하신 아이디가 없습니다 \n 다시 확인하세요";
		var passerror = "입력하신 비밀번호가 다릅니다 \n 다시 확인하세요";
		var deleteerror = "회원탈퇴에 실패했습니다 \n 잠시 후 다시 시도하세요";
		var modifyerror = "회원정보수정에 실패했습니다 \n 잠시 후 다시 시도하세요";
		
		
		function erroralert(msg) {
			alert(msg);
			history.back();
		}
		
		
		
		// 아이디 중복확인
		$("input[value='중복확인']").on(
			"click",
			function(event) {
				var user_id = $("input[name='user_id']").val();
				if(! user_id) {
					alert(iderror);
					inputform.user_id.focus();
				} else {
					url="confirmId?user_id=" + user_id;
					open(url,"confirmId","scrollbar=no, statusbar=no, titlebar=no, menubar=no, width=400px, height=250px");
				}	
			} // function
		); // on
		
		$("input[value='확인']").on(
			"click",
			function(event){
				if(! $("input[name='user_id']").val()) {
					alert(iderror);
					confirmform.user_id.focus();
					return false;
				}
			} // function
		); // on
		
		function close(){
			window.open('','_self').close();
		}

		$("input[value='사용']").on(
			"click",
			function(event) {
				opener.document.inputform.user_id.value = $("td span").text();
				opener.document.inputform.check.value="1";
				window.open('','_self').close();
			}
		);
		
		
		
		// 회원정보수정
		function modifycheck() {
			if(! modifyform.user_passwd.value) {
				alert(passwderror);
				modifyform.user_passwd.focus();
				return false;
			} else if (modifyform.user_passwd.value != modifyform.user_repasswd.value) {
				alert(repasswderror);
				modifyform.user_passwd.focus();
				return false;
			}
		}
		
		
		// 회원정보수정
		$("input[value='수정']").on(
			"click",
			function passwdcheck() {
				if(! passwdform.user_passwd.value) {
					alert(passwderror);
					passwdform.user_passwd.focus();
					return false;
				}
			}
		); // on
		
		
		
		// 회원탈퇴
		$("input[value='탈퇴']").on(
			"click",
			function passwdcheck() {
				if(! passwdform.user_passwd.value) {
					alert(passwderror);
					passwdform.user_passwd.focus();
					return false;
				}
			}
		); // on
		
		
		
		
		// 가입페이지
		$("form[name='inputform']").on(
			"submit",
			function() {
				if( inputform.check.value == "0" ) {
					alert(confirmerror);
					inputform.user_id.focus();
					return false;
				}
				
				if(! $("input[name='user_id']").val()) {
					alert(iderror);
					inputform.user_id.focus();
					return false;
				} else if(! $("input[name='user_passwd']").val()) {
					alert(passwderror);
					inputform.user_passwd.focus();
					return false;
				} else if($("input[name='user_passwd']").val() != $("input[name='user_repasswd']").val()) {
					alert(repasswderror);
					inputform.user_passwd.value = "";
					inputform.user_passwd.focus();
					return false;
				} else if(! $("input[name='user_name']").val()) {
					alert(nameerror);
					inputform.user_name.focus();
					return false;
				} else if(! $("input[name='user_email']").val()) {
					alert(emailerror);
					inputform.user_email.focus();
					return false;
				}  else if(! $("input[name='user_tel']").val()) {
					alert(telerror);
					inputform.user_tel.focus();
					return false;
				}

			}	//function
		);	//on
		

		
		// 로그인
		$("form[name='loginform']").on(
			"submit",
			function(event) {
				if(! $("input[name='user_id']").val()) {
					alert(iderror);
					$("input[name='user_id']").focus();
					return false;
				} else if (! $("input[name='user_passwd']").val()) {
					alert(passwderror);
					$("input[name='user_passwd']").focus();
					return false;
				}
			}	
		);
		
		// 포인트충전
		$("input[id='charge']").on(
			"click",
			function(event) {
				if(! $("input[name='point']").val()) {
					alert(pointerror);
					$("input[name='point']").focus();
					return false;
				} 
				
			}
			
		);	// on
		
		
		
		// 리뷰작성
		$("button[id='write']").on(
			"click",
			function(event) {
				if(! reviewwrite.rating.value) {
					alert(ratingerror);
					reviewwrite.rating.focus();
					return false;
				} else if(! reviewwrite.content.value) {
					alert(reviewerror);
					reviewwrite.content.focus();
					return false;
				}
			}
			
		);
		
		
		
		
		
		
		
		
		
		
	
	}	// function
);	// ready
