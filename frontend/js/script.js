// Get references to the form and the input field
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");
const chatWindow = document.getElementById("chat-log");

// Runs when the user clicks "Send" or presses Enter
chatForm.addEventListener("submit", (event) => {
    // Prevent the browser from reloading the page
    event.preventDefault();

    // Read the message and ignore empty input
    const input = chatInput.value.trim();
    if (input === "") {
        return;
    }
    // Show the user's own message in the chat log right away
    addMessageToWindow(input);
    sendMessage(input);
    
    

    // Clear the input field
    chatInput.value = "";
});

async function sendMessage(input) {
    // TODO: chat functionality is not implemented yet.
    // Later: send `message` to the backend and show the answer in #chat-log.
    console.log("Message (not sent yet):", input);

    try {
        const result = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: input})
        });
        const output = await result.json();
        console.log("Return message:", output);
        // The backend answers with {"response": "..."}
        addMessageToWindow(output.response);
        return true;
    } catch (_) {
        console.log("Error")
        return false
    }
}

function addMessageToWindow(msg) {
    const div = document.createElement('div');
    // textContent is a property, not a function: assign to it
    div.textContent = msg;
    chatWindow.appendChild(div);
    return div;
}
