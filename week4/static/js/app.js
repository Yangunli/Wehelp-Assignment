
let square=document.querySelector("#square")
let btn = document.querySelector(".btn")



function submitBtn(value) {
    let str =""
    let submitValue = square.value
    str = submitValue
    result = str*str
}

const res = fetch('http://127.0.0.1:3000/', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
    },
    credentials: 'include'
}).then(response => {
    if(response.status == 200){
        console.log('Success! ' + response.json() )
    }
}).catch(error => {
    console.log('error with access token req!')
})

console.log(res)



btn.addEventListener("click", submitBtn);
