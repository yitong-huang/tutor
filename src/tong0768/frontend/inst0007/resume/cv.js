function submitComment() {
    var comment = document.getElementById("comment-input").value;
    var name = document.getElementById("name-input").value;

    if (comment == "") {
        alert("Please input comment");
        return;
    }
    if (name == "") {
        alert("Please input your name");
        return;
    }

    var card = document.createElement("div");
    card.setAttribute("class", "card") 
    
    var cardTitle = document.createElement("p");
    cardTitle.innerText = name;
    cardTitle.setAttribute("class", "card-title");
    card.appendChild(cardTitle);

    var cardContent = document.createElement("p");
    cardContent.innerText = comment;
    card.appendChild(cardContent);

    var commentCard = document.getElementById("comment-card");

    document.getElementsByClassName("main-right")[0].insertBefore(card, commentCard);
}