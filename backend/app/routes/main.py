# backend/app/routes/main.py
from flask import Blueprint, jsonify, request
from app.models.artist import Artist
from app.models.venue import Venue
from app.models.booking import Booking
from app import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to VenueMath API!"})

@bp.route('/artists', methods=['GET'])
def get_artists():
    try:
        artists = Artist.query.all()
        return jsonify([artist.to_dict() for artist in artists])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    try:
        artist = Artist.query.get_or_404(id)
        return jsonify(artist.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@bp.route('/venues', methods=['GET'])
def get_venues():
    try:
        venues = Venue.query.all()
        return jsonify([venue.to_dict() for venue in venues])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/venues/<int:id>', methods=['GET'])
def get_venue(id):
    try:
        venue = Venue.query.get_or_404(id)
        return jsonify(venue.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@bp.route('/bookings', methods=['GET'])
def get_bookings():
    try:
        bookings = Booking.query.all()
        return jsonify([booking.to_dict() for booking in bookings])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@bp.route('/dashboard/<int:artist_id>', methods=['GET'])
def get_dashboard_data(artist_id):
    try:
        # Get artist
        artist = Artist.query.get_or_404(artist_id)
        
        # Get upcoming bookings
        upcoming_bookings = Booking.query.filter_by(
            artist_id=artist_id,
            status='confirmed'
        ).filter(
            Booking.event_date >= datetime.utcnow()
        ).all()
        
        # Calculate potential earnings
        potential_earnings = sum(booking.price for booking in upcoming_bookings)
        
        # Get matched venues (simple matching based on location)
        matched_venues = Venue.query.filter_by(
            location=artist.location
        ).limit(5).all()
        
        return jsonify({
            'stats': {
                'upcoming_gigs': len(upcoming_bookings),
                'potential_earnings': potential_earnings,
                'rating': 4.9,
                'messages': 3
            },
            'matched_venues': [venue.to_dict() for venue in matched_venues],
            'upcoming_bookings': [booking.to_dict() for booking in upcoming_bookings]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
