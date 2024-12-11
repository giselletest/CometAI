# backend/app/seed.py
from app import create_app, db
from app.models.artist import Artist
from app.models.venue import Venue
from app.models.booking import Booking
from datetime import datetime, timedelta

def seed_database():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create Artists
        artists = [
            Artist(
                name="Your Band Name",
                email="yourband@email.com",
                genre="Rock/Alternative",
                bio="Local alternative rock band from SF Bay Area",
                location="San Francisco, CA"
            ),
            Artist(
                name="Jazz Quartet",
                email="jazzquartet@email.com",
                genre="Jazz",
                bio="Contemporary jazz ensemble",
                location="Oakland, CA"
            ),
            Artist(
                name="The Local Beats",
                email="localbeats@email.com",
                genre="Hip-Hop",
                bio="Underground hip-hop collective",
                location="Berkeley, CA"
            )
        ]
        
        # Create Venues
        venues = [
            Venue(
                name="The Independent",
                email="independent@venue.com",
                venue_type="Concert Hall",
                capacity=500,
                location="San Francisco, CA",
                description="Historic San Francisco music venue",
                amenities={
                    "sound_system": True,
                    "stage": True,
                    "green_room": True,
                    "parking": True
                }
            ),
            Venue(
                name="Yoshi's Oakland",
                email="yoshis@venue.com",
                venue_type="Jazz Club",
                capacity=310,
                location="Oakland, CA",
                description="Premier jazz venue and Japanese restaurant",
                amenities={
                    "sound_system": True,
                    "stage": True,
                    "restaurant": True,
                    "parking": True
                }
            ),
            Venue(
                name="Bottom of the Hill",
                email="bottomhill@venue.com",
                venue_type="Rock Club",
                capacity=250,
                location="San Francisco, CA",
                description="Intimate rock club venue",
                amenities={
                    "sound_system": True,
                    "stage": True,
                    "bar": True
                }
            )
        ]
        
        # Create some past and upcoming bookings
        now = datetime.utcnow()
        bookings = [
            Booking(
                artist=artists[0],
                venue=venues[0],
                event_date=now + timedelta(days=7),
                status='confirmed',
                price=350.00,
                notes="Opening act, 45-minute set"
            ),
            Booking(
                artist=artists[0],
                venue=venues[2],
                event_date=now + timedelta(days=14),
                status='pending',
                price=300.00,
                notes="Headlining show"
            ),
            Booking(
                artist=artists[1],
                venue=venues[1],
                event_date=now + timedelta(days=3),
                status='confirmed',
                price=400.00,
                notes="Jazz night performance"
            )
        ]
        
        # Add to database
        for artist in artists:
            db.session.add(artist)
        for venue in venues:
            db.session.add(venue)
        for booking in bookings:
            db.session.add(booking)
            
        # Commit changes
        db.session.commit()
        
        print("Database seeded!")

if __name__ == '__main__':
    seed_database()
