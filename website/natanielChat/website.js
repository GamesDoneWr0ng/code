let websocket;
 
function setupWebSocket() {
    websocket = new WebSocket('ws://172.20.2.115:5003');
 
    websocket.onopen = () => {
        console.log('Connected to server');
    };
 
    websocket.onmessage = (event) => {
        console.log('Received:', event.data);
    };
 
    websocket.onerror = (err) => {
        console.error('WebSocket error:', err);
    };
 
    websocket.onclose = () => {
        console.log('Connection closed');
    };
}
 
function sendMessage(message) {
    if (websocket && websocket.readyState === WebSocket.OPEN) {
        websocket.send(message);
        console.log('Sent:', message);
    } else {
        console.error('WebSocket is not open');
    }
}
 
// Attach event listeners to the webpage
document.addEventListener('DOMContentLoaded', () => {
    setupWebSocket();
 
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
 
    sendButton.addEventListener('click', () => {
        const message = messageInput.value;
        sendMessage(message);
    });
});