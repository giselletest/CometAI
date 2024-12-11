# app/models/venue.py
from app import db
from datetime import datetime

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    venue_type = db.Column(db.String(64))
    capacity = db.Column(db.Integer)
    location = db.Column(db.String(120))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    bookings = db.relationship('Booking', backref='venue', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'venue_type': self.venue_type,
            'capacity': self.capacity,
            'location': self.location,
            'description': self.description
        }
