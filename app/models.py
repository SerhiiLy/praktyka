from . import db


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.Integer, unique=True, nullable=False)
    departure_time = db.Column(db.Text, nullable=False)
    day_week = db.Column(db.Text, nullable=False)
    number_seats = db.Column(db.Integer, nullable=False)
    route = db.Column(db.Text, nullable=False)
