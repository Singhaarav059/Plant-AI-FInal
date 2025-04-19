// forum.js - Functionality for the forum/community page

document.addEventListener('DOMContentLoaded', function() {
    // Initialize forum features
    initForumInteractions();
});

/**
 * Initialize forum interactions
 */
function initForumInteractions() {
    // Toggle comment sections
    const commentToggles = document.querySelectorAll('.toggle-comments');
    
    commentToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            
            const postId = this.getAttribute('data-post-id');
            const commentSection = document.getElementById(`comments-${postId}`);
            
            if (commentSection) {
                // Toggle visibility
                if (commentSection.style.display === 'none' || !commentSection.style.display) {
                    commentSection.style.display = 'block';
                    this.textContent = this.getAttribute('data-hide-text') || 'Hide Comments';
                } else {
                    commentSection.style.display = 'none';
                    this.textContent = this.getAttribute('data-show-text') || 'View Comments';
                }
            }
        });
    });
    
    // New post form toggle
    const newPostBtn = document.getElementById('new-post-btn');
    const newPostForm = document.getElementById('new-post-form');
    
    if (newPostBtn && newPostForm) {
        newPostBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            if (newPostForm.style.display === 'none' || !newPostForm.style.display) {
                newPostForm.style.display = 'block';
                this.textContent = this.getAttribute('data-hide-text') || 'Cancel';
            } else {
                newPostForm.style.display = 'none';
                this.textContent = this.getAttribute('data-show-text') || 'Create New Post';
                
                // Clear form fields
                document.getElementById('post-title').value = '';
                document.getElementById('post-content').value = '';
            }
        });
    }
    
    // Form validation
    const postForm = document.getElementById('post-form');
    if (postForm) {
        postForm.addEventListener('submit', function(e) {
            const title = document.getElementById('post-title').value.trim();
            const content = document.getElementById('post-content').value.trim();
            
            if (!title || !content) {
                e.preventDefault();
                alert('Please fill in both title and content fields');
            }
        });
    }
    
    // Comment form validation
    const commentForms = document.querySelectorAll('.comment-form');
    commentForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const commentContent = this.querySelector('textarea').value.trim();
            
            if (!commentContent) {
                e.preventDefault();
                alert('Comment cannot be empty');
            }
        });
    });
}

/**
 * Add a new comment to a post (without page reload)
 * This function would be used for AJAX comment submission
 * Currently not implemented as the server uses form submission
 */
function addComment(postId, content) {
    // This would be an AJAX implementation
    // For now, we're using form submission with page reload
    
    fetch(`/post/${postId}/comment`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `content=${encodeURIComponent(content)}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Append new comment to the comment section
            const commentSection = document.getElementById(`comments-${postId}`);
            const newComment = createCommentElement(data.comment);
            commentSection.appendChild(newComment);
            
            // Clear input
            document.querySelector(`#comment-form-${postId} textarea`).value = '';
        } else {
            alert('Error adding comment: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while adding your comment');
    });
}

/**
 * Create a comment element (helper for AJAX implementation)
 */
function createCommentElement(comment) {
    const commentDiv = document.createElement('div');
    commentDiv.className = 'card mb-2';
    
    commentDiv.innerHTML = `
        <div class="card-body py-2">
            <p class="card-text">${comment.content}</p>
            <p class="card-text"><small class="text-muted">Posted by ${comment.username} on ${comment.timestamp}</small></p>
        </div>
    `;
    
    return commentDiv;
}
