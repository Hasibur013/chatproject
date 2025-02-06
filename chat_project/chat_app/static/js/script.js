document.getElementById("chat-form").addEventListener("submit", function (e) {
    e.preventDefault();

    let formData = new FormData();
    formData.append("text", document.getElementById("text-input").value);
    formData.append("image", document.getElementById("image-input").files[0]);
    formData.append("audio", document.getElementById("audio-input").files[0]);

    fetch("/send/", {
        method: "POST",
        body: formData,
        headers: { "X-CSRFToken": getCSRFToken() }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            location.reload();
        }
    });
});

function getCSRFToken() {
    return document.cookie.split("; ").find(row => row.startsWith("csrftoken")).split("=")[1];
}

// Auto-resize textarea
function autoResize(element) {
    element.style.height = 'auto';
    element.style.height = (element.scrollHeight) + 'px';
}

// Scroll to bottom of chat box
function scrollToBottom() {
    const chatBox = document.getElementById("chat-box");
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Scroll to bottom when new messages are added
scrollToBottom();