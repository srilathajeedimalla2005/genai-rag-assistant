const sendBtn = document.getElementById("send-btn")

const userInput = document.getElementById("user-input")

const chatBox = document.getElementById("chat-box")


function addMessage(text,type){

let message=document.createElement("div")

message.classList.add("message",type)

message.innerText=text

chatBox.appendChild(message)

chatBox.scrollTop=chatBox.scrollHeight

}


sendBtn.onclick=sendMessage

userInput.addEventListener("keypress",function(e){

if(e.key==="Enter"){

sendMessage()

}

})


async function sendMessage(){

let text=userInput.value.trim()

if(text==="") return

addMessage(text,"user")

userInput.value=""

let response=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({message:text})

})

let data=await response.json()

addMessage(data.reply,"bot")

}