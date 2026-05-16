function sendMessage() {
    let inputField = document.getElementById("user-input");
    let message = inputField.value.trim();
    
    if(message === "") return;
    
    let chatBox = document.getElementById("chat-box");
    
    let userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);
    
    chatBox.scrollTop = chatBox.scrollHeight;
    
    let typingDiv = document.createElement("div");
    typingDiv.className = "bot-message typing-indicator";
    typingDiv.innerHTML = "<span></span><span></span><span></span>";
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    fetch("/get", {
        method: "POST",
        headers: {
            "Content-Type":"application/x-www-form-urlencoded"
        },
        body: "message=" + encodeURIComponent(message)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        chatBox.removeChild(typingDiv);
        
        setTimeout(() => {
            let botDiv = document.createElement("div");
            botDiv.className = "bot-message";
            botDiv.innerText = data.reply;
            chatBox.appendChild(botDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }, 400);
    })
    .catch(error => {
        console.error('Error:', error);
        chatBox.removeChild(typingDiv);
        let errorDiv = document.createElement("div");
        errorDiv.className = "bot-message";
        errorDiv.innerText = "Oops, something went wrong. Please try again!";
        chatBox.appendChild(errorDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
    
    inputField.value = "";
}

document.getElementById("user-input").addEventListener("keypress", function(e){
    if(e.key === "Enter"){
        sendMessage();
    }
});

function quickMessage(text){
    document.getElementById("user-input").value = text;
    sendMessage();
}