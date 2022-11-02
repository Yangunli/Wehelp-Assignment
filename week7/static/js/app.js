const container = document.querySelector("body")
const searchMemberEl = document.querySelector("#searchMember")
const memberEl = document.createElement("h4")

function getUsername()
{
let username=document.querySelector("#inputUsername").value
fetch(`http://127.0.0.1:3000/api/member?username=${username}`) .then(function(response) {
  return response.json()
})
.then(function(myJson) {
  if(myJson.data?.username){
  let username =myJson.data.username
  let name = myJson.data.name.toUpperCase()
  memberEl.textContent=`${name}( ${username})`
}else{
  memberEl.textContent = `查無此人`
}
  searchMemberEl.appendChild(memberEl)

});
}