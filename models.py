from app import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    detections = db.relationship('DiseaseDetection', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    # Relationships
    comments = db.relationship('Comment', backref='post', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Post {self.title}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Comment {self.id}>'

class DiseaseDetection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_data = db.Column(db.Text, nullable=False)  # Base64 encoded image data
    disease_name = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    severity = db.Column(db.String(20), nullable=False)  # 'low', 'medium', 'high'
    description = db.Column(db.Text, nullable=False)
    treatment = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Detection {self.disease_name}>'
