from dotenv import load_dotenv
import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import base64
from datetime import datetime
from translations import get_translations
from chatbot import get_response
import uuid
import json

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Initialize database
db = SQLAlchemy(model_class=Base)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

# Configure the database
database_url = os.environ.get("DATABASE_URL", "sqlite:///plantdisease.db")
# Fix for Render PostgreSQL URLs
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the database with the app
db.init_app(app)

# Import models after db initialization (but before create_all)
# Moved import here to avoid circular import
# Image upload configuration
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

with app.app_context():
    import models
    # Create all database tables
    db.create_all()

# In-memory storage for forum posts and comments (to be used as a fallback)
forum_storage = {'posts': [], 'comments': {}}

# Load ML model
from ml_model import load_model, preprocess_image, predict_disease

# Create all database tables
with app.app_context():
    db.create_all()
    
# Languages supported by the application
LANGUAGES = {
    'en': 'English',
    'hi': 'हिन्दी (Hindi)',
    'ta': 'தமிழ் (Tamil)',
    'te': 'తెలుగు (Telugu)',
    'bn': 'বাংলা (Bengali)',
    'gu': 'ગુજરાતી (Gujarati)'
}

# Routes
@app.route('/')
def index():
    """Home page route"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    return render_template('index.html', translations=translations, languages=LANGUAGES)

@app.route('/set_language/<lang>')
def set_language(lang):
    """Set the user's preferred language"""
    if lang in LANGUAGES:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/detect', methods=['POST'])
def detect_disease():
    """Handle image upload and disease detection"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if 'plant_image' not in request.files:
        flash(translations['no_file_selected'], 'error')
        return redirect(url_for('index'))
    
    file = request.files['plant_image']
    
    if file.filename == '':
        flash(translations['no_file_selected'], 'error')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        # Convert image to base64 for temporary storage
        img_data = file.read()
        base64_img = base64.b64encode(img_data).decode('utf-8')
        
        # Process the image for prediction
        try:
            # Preprocess image and make prediction with OpenAI Vision
            # Pass user's language preference to get response in the right language
            processed_img = preprocess_image(img_data)
            disease_name, confidence, severity, description, treatment = predict_disease(processed_img, lang)
            
            # Save the detection result to database if user is logged in
            if 'user_id' in session:
                detection = DiseaseDetection(
                    user_id=session['user_id'],
                    image_data=base64_img,
                    disease_name=disease_name,
                    confidence=confidence,
                    severity=severity,
                    description=description,
                    treatment=treatment,
                    timestamp=datetime.now()
                )
                db.session.add(detection)
                db.session.commit()
            
            return render_template(
                'disease_result.html',
                translations=translations,
                languages=LANGUAGES,
                image=base64_img,
                disease=disease_name,
                confidence=confidence,
                severity=severity,
                description=description,
                treatment=treatment
            )
            
        except Exception as e:
            logging.error(f"Error processing image: {str(e)}")
            flash(translations['error_processing'], 'error')
            return redirect(url_for('index'))
    else:
        flash(translations['invalid_file_type'], 'error')
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash(translations['user_exists'], 'error')
            return redirect(url_for('register'))
        
        # Create new user
        new_user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password)
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash(translations['registration_success'], 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error registering user: {str(e)}")
            flash(translations['registration_error'], 'error')
    
    return render_template('register.html', translations=translations, languages=LANGUAGES)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(translations['login_success'], 'success')
            return redirect(url_for('index'))
        else:
            flash(translations['invalid_credentials'], 'error')
    
    return render_template('login.html', translations=translations, languages=LANGUAGES)

@app.route('/logout')
def logout():
    """User logout"""
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/forum')
def forum():
    """Forum/discussion page"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    try:
        posts = Post.query.order_by(Post.timestamp.desc()).all()
    except Exception as e:
        logging.error(f"Error fetching forum posts: {str(e)}")
        posts = []
        # Use in-memory storage as fallback
        for post in forum_storage['posts']:
            posts.append(post)
    
    return render_template('forum.html', translations=translations, languages=LANGUAGES, posts=posts)

@app.route('/create_post', methods=['POST'])
def create_post():
    """Create a new forum post"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if 'user_id' not in session:
        flash(translations['login_required'], 'error')
        return redirect(url_for('login'))
    
    title = request.form.get('title')
    content = request.form.get('content')
    
    if not title or not content:
        flash(translations['incomplete_fields'], 'error')
        return redirect(url_for('forum'))
    
    try:
        new_post = Post(
            user_id=session['user_id'],
            title=title,
            content=content,
            timestamp=datetime.now()
        )
        db.session.add(new_post)
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error creating post: {str(e)}")
        # Add to in-memory storage as a fallback
        post_id = str(uuid.uuid4())
        post = {
            'id': post_id,
            'user_id': session['user_id'],
            'username': session['username'],
            'title': title,
            'content': content,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        forum_storage['posts'].append(post)
        forum_storage['comments'][post_id] = []
        
    flash(translations['post_created'], 'success')
    return redirect(url_for('forum'))

@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    """Add a comment to a forum post"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if 'user_id' not in session:
        flash(translations['login_required'], 'error')
        return redirect(url_for('login'))
    
    content = request.form.get('content')
    
    if not content:
        flash(translations['empty_comment'], 'error')
        return redirect(url_for('forum'))
    
    try:
        new_comment = Comment(
            post_id=post_id,
            user_id=session['user_id'],
            content=content,
            timestamp=datetime.now()
        )
        db.session.add(new_comment)
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error adding comment: {str(e)}")
        # Add to in-memory storage as fallback
        comment = {
            'id': str(uuid.uuid4()),
            'post_id': post_id,
            'user_id': session['user_id'],
            'username': session['username'],
            'content': content,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        if str(post_id) in forum_storage['comments']:
            forum_storage['comments'][str(post_id)].append(comment)
        else:
            forum_storage['comments'][str(post_id)] = [comment]
    
    flash(translations['comment_added'], 'success')
    return redirect(url_for('forum'))

@app.route('/api/chatbot', methods=['POST'])
def chatbot_api():
    """API endpoint for chatbot interactions"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    data = request.json
    question = data.get('message', '')
    
    if not question:
        return jsonify({
            'status': 'error',
            'message': translations['empty_question']
        })
    
    response = get_response(question, lang)
    
    return jsonify({
        'status': 'success',
        'message': response
    })

@app.route('/history')
def history():
    """View user's disease detection history"""
    lang = session.get('language', 'en')
    translations = get_translations(lang)
    
    if 'user_id' not in session:
        flash(translations['login_required'], 'error')
        return redirect(url_for('login'))
    
    detections = DiseaseDetection.query.filter_by(user_id=session['user_id']).order_by(DiseaseDetection.timestamp.desc()).all()
    
    return render_template(
        'history.html',
        translations=translations,
        languages=LANGUAGES,
        detections=detections
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
