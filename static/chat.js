async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() !== "") {
        addMessage(userInput, "user-message");

        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userInput })
        });
        const result = await response.json();

        addMessage(result.response, "bot-message");
        document.getElementById("user-input").value = '';
    }
}

function addMessage(text, className) {
    const chatBox = document.getElementById("chat-box");
    const message = document.createElement("div");
    message.className = className;
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}
