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

    // Ajax
    const request = new XMLHttpRequest();
    const url = "https://inst0007.2fish.com.cn/sendmail?name=" + encodeURIComponent(name) + "&comment=" + encodeURIComponent(comment)
    request.open("GET", url);
    request.send();
    request.onloadend = (e) => {
        if (request.status == 200) {
            alert(request.responseText)
        } else {
            alert("Oops, something wrong with the server")
        }
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

    // var subject = name + " Leave Message On Your Page";
    // var url = "mailto:yitong0768@gmail.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(comment);
    // window.open(url)
} 