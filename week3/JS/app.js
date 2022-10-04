const titleContainer = document.querySelector(".title-container")
const getData = fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
.then(function (response) {
    return response.json()
})
.then(function (myJson) {
    let data = myJson.result.results
    for (let i = 0; i < 10; i++) {
        const title = document.createElement("div");
        title.setAttribute("class", "title");
        document.querySelector(".title-container").appendChild(title);
        let view = data[i];
        let imgUrl = `htt${view.file.split("htt")[1]}`;
        let stitle = view.stitle;
        let viewImg = document.createElement("img");
        let viewTitle = document.createElement("p");
        let star= document.createElement("div")
        star.setAttribute("class","star-icons")
        title.appendChild(star)
        title.appendChild(viewImg);
        title.appendChild(viewTitle);
        viewImg.setAttribute("src", imgUrl);
        viewTitle.textContent = stitle;
    }
});
