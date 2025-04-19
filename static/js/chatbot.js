// chatbot.js - Functionality for the chatbot feature

document.addEventListener('DOMContentLoaded', function() {
    // Initialize chatbot
    initChatbot();
});

/**
 * Initialize chatbot functionality
 */
function initChatbot() {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-message');
    
    // If chatbot elements don't exist, return
    if (!chatContainer || !messageInput || !sendButton) return;
    
    // Add initial bot greeting if element exists
    const botGreetingElement = document.getElementById('bot-greeting');
    if (botGreetingElement) {
        const botGreeting = botGreetingElement.textContent;
        addMessage(botGreeting, 'bot');
    }
    
    // Send message when button is clicked
    sendButton.addEventListener('click', sendMessage);
    
    // Send message when Enter key is pressed
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    function sendMessage() {
        const message = messageInput.value.trim();
        
        if (message) {
            // Add user message to chat
            addMessage(message, 'user');
            
            // Clear input
            messageInput.value = '';
            
            // Send to server and get response
            fetchBotResponse(message);
        }
    }
    
    function addMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.className = `chat-message ${sender}-message`;
        messageElement.textContent = message;
        
        chatContainer.appendChild(messageElement);
        
        // Scroll to bottom
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    
    function fetchBotResponse(message) {
        // Show loading indicator
        addMessage('...', 'bot');
        
        fetch('/api/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remove loading indicator
            chatContainer.removeChild(chatContainer.lastChild);
            
            if (data.status === 'success') {
                addMessage(data.message, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        })
        .catch(error => {
            // Remove loading indicator
            chatContainer.removeChild(chatContainer.lastChild);
            
            console.error('Error:', error);
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        });
    }
}
