from database import db

class User(db.Model):
    id = db.Column("userId", db.Integer, primary_key = True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    rsvp = db.relationship("Attendance", backref="user", lazy = True)
    event = db.relationship("Event", backref="user", lazy = True)
    ratings = db.relationship("Ratings", backref="user", lazy = True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Event(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    event_name = db.Column("event_name", db.String(200))
    event_info = db.Column("event_info", db.String(500))
    date = db.Column("date", db.String(50))
    event_location = db.Column("event_location", db.String(100))
    rsvp = db.relationship("Attendance", backref="event", lazy = True)
    ratings = db.relationship("Ratings", backref="event", cascade="all, delete-orphan", lazy = True)

    def __init__(self, event_name, event_info, date, event_location,):
        self.event_name = event_name
        self.event_info = event_info
        self.date = date
        self.event_location = event_location



class Ratings(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable = False)

    def __init__(self, rating, user_id, event_id):
        self.rating = rating
        self.user_id = user_id
        self.event_id = event_id



class Attendance(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    rsvp = db.Column("rsvp", db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    event_id = db.Column(db.Integer, db.ForeignKey("event.id"), nullable = False)

    def __init__(self, rsvp, user_id, event_id):
        self.rsvp = rsvp
        self.user_id = user_id
        self.event_id = event_id
