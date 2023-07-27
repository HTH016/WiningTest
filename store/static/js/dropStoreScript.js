const btnCheck = document.getElementById("btnCheck");

btnCheck.addEventListener("click", () => {
    const url = "/store/drop-store";
    const passwd = document.getElementById("passwd").value;

    console.log(passwd);

    const init = {
        method: "POST",
        header: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            passwd: passwd,
        }),
    };

    fetch(url, init)
        .then((response) => response.json())
        .then((data) => {
            let responseData = data

            if (responseData["code"] == -1) {
                alert(responseData["result"])
                console.log("비밀번호가 달라")
                return false
            }
            else if (responseData["code"] == 1) {
                alert(responseData["result"])
                console.log("비밀번호가 맞아")
                //유저 마이페이지로 리다이렉트
            }
        })

})
function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

