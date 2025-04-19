// main.js - Core functionality for the Plant Disease Detection Website

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize file upload preview
    initImageUpload();
    
    // Initialize chatbot if chat container exists
    if (document.getElementById('chat-container')) {
        initChatbot();
    }
});

/**
 * Initialize image upload functionality
 */
function initImageUpload() {
    const fileInput = document.getElementById('plant-image');
    const uploadForm = document.getElementById('upload-form');
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('preview-image');
    const uploadArea = document.querySelector('.upload-area');
    
    // If elements don't exist, return
    if (!fileInput || !uploadForm) return;
    
    // Handle file selection
    fileInput.addEventListener('change', function() {
        if (fileInput.files && fileInput.files[0]) {
            const file = fileInput.files[0];
            
            // Check file type
            const validTypes = ['image/jpeg', 'image/jpg', 'image/png'];
            if (!validTypes.includes(file.type)) {
                alert('Please select a valid image file (JPG, JPEG, PNG)');
                fileInput.value = '';
                return;
            }
            
            // Display preview
            const reader = new FileReader();
            reader.onload = function(e) {
                previewImage.src = e.target.result;
                previewContainer.style.display = 'block';
                
                // Enable the submit button
                document.querySelector('button[type="submit"]').disabled = false;
            }
            reader.readAsDataURL(file);
        }
    });
    
    // Handle drag and drop
    if (uploadArea) {
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            uploadArea.addEventListener(eventName, highlight, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            uploadArea.addEventListener(eventName, unhighlight, false);
        });
        
        function highlight() {
            uploadArea.classList.add('dragover');
        }
        
        function unhighlight() {
            uploadArea.classList.remove('dragover');
        }
        
        uploadArea.addEventListener('drop', handleDrop, false);
        
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            
            if (files && files.length) {
                fileInput.files = files;
                // Trigger change event
                const event = new Event('change');
                fileInput.dispatchEvent(event);
            }
        }
    }
}

/**
 * Initialize chatbot functionality
 */
function initChatbot() {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-message');
    
    // Add initial bot greeting
    const botGreeting = document.getElementById('bot-greeting').textContent;
    addMessage(botGreeting, 'bot');
    
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
        fetch('/api/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                addMessage(data.message, 'bot');
            } else {
                addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage('Sorry, I encountered an error. Please try again.', 'bot');
        });
    }
}
