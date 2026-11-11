// Get references to the form and the input field
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

// Runs when the user clicks "Send" or presses Enter
chatForm.addEventListener("submit", (event) => {
    // Prevent the browser from reloading the page
    event.preventDefault();

    // Read the message and ignore empty input
    const message = chatInput.value.trim();
    if (message === "") {
        return;
    }

    // TODO: chat functionality is not implemented yet.
    // Later: send `message` to the backend and show the answer in #chat-log.
    console.log("Message (not sent yet):", message);

    // Clear the input field
    chatInput.value = "";
});
