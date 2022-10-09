const container = document.querySelector(".container");
const promotionContainer = document.createElement("div")
const titleContainer =  document.createElement("div")
promotionContainer.setAttribute("class","promotion-container")
titleContainer.setAttribute("class","title-container")
container.appendChild(promotionContainer)
container.appendChild(titleContainer)
const loadBtn = document.createElement("button")
loadBtn.setAttribute("class", "loadBtn")
loadBtn.textContent="Load More"
container.appendChild(loadBtn)

fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response) {
    return response.json();
  }).then(function(myJson) {
    let data=(myJson.result.results)
    for(let i=0; i<data.length; i++){
      let view = data[i]
      let imgUrl=`htt${view.file.split('htt')[1]}`
      let stitle =view.stitle
      let viewImg = document.createElement("img")
      let viewTitle = document.createElement("p")
      if(i <2){
        const promotion = document.createElement("div");
        promotion.setAttribute("class", "promotion");
        document.querySelector(".promotion-container").appendChild(promotion);
        promotion.appendChild(viewImg)
        promotion.appendChild(viewTitle)
        viewImg.setAttribute("src", imgUrl)
        viewTitle.textContent = stitle       
      }else{
        const title = document.createElement("div");
        title.setAttribute("class", "title");
        document.querySelector(".title-container").appendChild(title);
        title.appendChild(viewImg)
        title.appendChild(viewTitle)
        viewImg.setAttribute("src", imgUrl)
        viewTitle.textContent = stitle
        let currentTitle = 8;
        loadBtn.addEventListener("click", () => {
          let titles = [
            ...document.querySelectorAll(".title-container .title"),
          ];
          for (var i = currentTitle; i < currentTitle + 8; i++) {
            titles[i].style.display = "flex";
          }
          currentTitle += 8;
          if (currentTitle >= data.length-2) {
            loadBtn.style.display = "none";
          }  
        })       
      }  
    }
  }
)


