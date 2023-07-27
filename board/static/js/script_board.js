
$(document).ready(
	function() {
		
		// var writererror= "작성자를 입력하세요.";
		var subjecterror = "제목을 입력하세요.";
		var contenterror = "내용을 입력하세요.";
		var passwderror = "비밀번호를 입력하세요.";
		
		var inserterror = "글작성에 실패했습니다.\n 잠시 후 다시 시도하세요.";
		var modifyerror = "글 수정에 실패했습니다.\n 잠시 후 다시 시도하세요.";
		var deleteerror = "글 삭제에 실패했습니다.\n 잠시 후 다시 시도하세요.";
		
		var modifyalert = "글이 수정되었습니다.\n";
		var deletealert = "글이 삭제되었습니다.\n"
		
		var passerror = "입력하신 비밀번호가 다릅니다.\n 다시 확인하세요";
		var replyerror = "댓글이 있는 글은 삭제할 수 없습니다.";
		
		
		
		
		function erroralert(msg){
			alert(msg);
			history.back();
		}
		
		//글수정
		$("form[name='updateform']").on(
			"submit",
			function (event) {
				if(! $("input[name='subject']").val() ) {
					alert(subjecterror);
					updateform.subject.focus();
					return false;
				}else if(! $("textarea[name='content']").val() ) {
					alert(contenterror);
					updateform.content.focus();
					return false;
				}else if(!  $("input[name='passwd']").val()  ) {
					alert(modifyalert);
					updateform.passwd.focus();
					return false;
				}
			}	
	);	
		
		//글삭제
		$("form[name='passwdform']").on(
			"submit",
			function (event) {
				if(! $("input[name='passwd']").val()  ) {
					alert(passwderror);
					passwdform.passwd.focus();
					return false;
				}
			}
		);
		
		
		
		//글쓰기
		$("form[name='writeform']").on(
			"submit",
			function (event ) {
			/*	if(! $("input[name='writer']").val() ) {
					alert(writererror);
					writeform.writer.focus();
					return false; 
				}else */ if(! $("input[name='subject']").val() ) {
					alert(subjecterror);
					writeform.subject.focus();
					return false;
				}else if(! $("textarea[name='content']").val() ) {
					alert(contenterror);
					writeform.content.focus();
					return false;
			/*	}else if(! $("input[name='passwd']").val() ) {
					alert(passwderror)
					writeform.passwd.focus();
					return false;	*/
				}else if( ! $("input[name='image']").val() ) {
					//alert("이미지를 선택하세요.."); 
					//return false;
					pass;
				}
			}
		); //on
		
		
		
		// 이미지 선택 시 미리보기
		$("input[name='image']").on("change", function () {
		  var input = $(this);
		  var imagePreview = $("#image-preview");
		
		  if (input && input[0].files && input[0].files[0]) {
		    var reader = new FileReader();
		
		    reader.onload = function (e) {
		      imagePreview.attr("src", e.target.result);
		    };
		
		    reader.readAsDataURL(input[0].files[0]);
		  }
		});
	
	
	
	
		// contentpro ?
	
		function redirectToContentPro() {
			var num = '{{ num }}';
			var pagenum = '{{pagenum}}';
			var number = '{{number}}';
			var url = 'contentpro?num=' + num + '&pagenum=' + pagenum + '&number=' + number;
			
			window.location.href = url;
		}
		
		$("input[name='확인']").on("click", function() {
			redirectToContentPro();
		});
		
	
		
		
	} //function
); //ready


