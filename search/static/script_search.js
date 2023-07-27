
 $(document).ready(
	function() {

		var searchnameerror = "검색어를 입력하세요.";

		
		var searcherror = "검색에 실패했습니다\n잠시 후 다시 시도하세요";

		

		function erroralert( msg ) {
			alert( msg );
			history.back();
		}
		
		
		// 이름 검색
		$("form[name='loginform']").on(
			"submit",
			function(event) {
				if(! $("input[name='searchName']").val()) {
					alert(searchnameerror);
					$("input[name='searchName']").focus();
					return false;
				} 
			}	
		);
	
/*		
		
		// 글수정
		$("form[name='updateform']").on(
			"submit",	
			function ( event ) {
				if( ! $("input[name='subject']").val() ) {
					alert( subjecterror );
					updateform.subject.focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					updateform.content.focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					updateform.passwd.focus();
					return false;
				}
			}
		);
		// 글삭제
		$("form[name='passwdform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					passwdform.passwd.focus();
					return false;
				}	
			}
		);
		// 글쓰기   
		$("form[name='writeform']").on(
			"submit",
			function( event ) {
				if( ! $("input[name='writer']").val() ) {
					alert( writererror );
					writeform.writer.focus();
					return false;
				} else if( ! $("input[name='subject'").val() ) {
					alert( subjecterror );
					writeform.subject.focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					writeform.content.focus();
					return false;
				} else if( ! $("input[name=passwd]").val() ) {
					alert( passwderror );
					writeform.passwd.focus();
					return false;
				}
			}		
		);	// on		

*/
	
	} // function
); // ready
		
