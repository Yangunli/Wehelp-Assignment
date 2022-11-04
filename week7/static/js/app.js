const container = document.querySelector("body");
const searchMemberEl = document.querySelector("#searchMemberContainer");
const updateNameContainerEl = document.querySelector("#updateNameContainer");

const memberEl = document.createElement("h4");

function getUsername() {
  let username = document.querySelector("#searchUsername").value;
  fetch(`http://127.0.0.1:3000/api/member?username=${username}`)
    .then((response) => response.json())
    .then(function (myJson) {
      if (myJson.data?.username) {
        let username = myJson.data.username;
        let name = myJson.data.name.toUpperCase();
        memberEl.textContent = `${name}( ${username})`;
      } else {
        memberEl.textContent = `查無此人`;
      }
      searchMemberEl.appendChild(memberEl);
    });
}

function getUpdateName() {
  let currentUsername = document
    .querySelector("#username")
    .innerText.split("，")[0]
    .toLowerCase();
  let newName = document.querySelector("#updateName").value;
  fetch(`http://127.0.0.1:3000/api/member/${currentUsername}`, {
    method: "PATCH",
    headers: {
      Accept: "application/json",
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      name: newName,
    }),
  }).then(function (response) {
    console.log(response);
    if (response.status !== 200) {
      memberEl.textContent = "更新失敗";
      updateNameContainerEl.appendChild(memberEl);
    } else {
      memberEl.textContent = "更新成功";
      updateNameContainerEl.appendChild(memberEl);
    }
  });
}
