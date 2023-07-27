let term = document.getElementById("term");
const listDiv = document.getElementById("revenueList");

term.addEventListener("change", () => {
    fetch("/store/store-revenue-term?term=" + term.value)
        .then((response) => response.json())
        .then((data) => {
            const responseData = data["result"];

            console.log(responseData);
            listDiv.replaceChildren();
            for (let i = 0; i < responseData.length; i++) {
                let values = new Map(Object.entries(responseData[i]));
                let date = values.get("date").substr(0, 7);
                let valueSum = values.get("value_sum");
                let qntySum = values.get("qnty_sum");

                const newRow = document.createElement("div");
                newRow.setAttribute("class", "row");

                const newDate = document.createElement("div");
                newDate.setAttribute("class", "col");
                newDate.innerText = date;

                const newValueSum = document.createElement("div");
                newValueSum.setAttribute("class", "col");
                newValueSum.innerText = valueSum + "원";

                const newQntySum = document.createElement("div");
                newQntySum.setAttribute("class", "col");
                newQntySum.innerText = qntySum + "개";


                listDiv.appendChild(newRow);
                newRow.appendChild(newDate);
                newRow.appendChild(newValueSum);
                newRow.appendChild(newQntySum);
            }
        })

})