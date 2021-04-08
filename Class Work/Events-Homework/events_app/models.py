"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    events_attending = db.relationship("Event", secondary="guest_events")


class PartyType(enum.Enum):
    Party = 1
    Study = 2
    Networking = 3


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date_and_time = db.Column(db.DateTime)
    event_type = db.Column(db.Enum(PartyType), default=PartyType.Party)
    guests = db.relationship("Guest", secondary="guest_events")


guest_event_table = db.Table(
    "guest_events",
    db.Column("event_id", db.Integer, db.ForeignKey("event.id")),
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id"))
)
