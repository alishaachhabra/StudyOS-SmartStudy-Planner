from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# ---------------- USER ---------------- #

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    dob = db.Column(
        db.String(20),
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    # Profile picture filename
    profile_pic = db.Column(
        db.String(255),
        default="default.png"
    )

    # Relationships
    subjects = db.relationship(
        "Subject",
        backref="user",
        cascade="all, delete",
        lazy=True
    )

    tasks = db.relationship(
        "Task",
        backref="user",
        cascade="all, delete",
        lazy=True
    )


# ---------------- SUBJECT ---------------- #

class Subject(db.Model):

    __tablename__ = "subjects"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    subject_name = db.Column(
        db.String(100),
        nullable=False
    )

    color = db.Column(
        db.String(20),
        nullable=False
    )

    icon = db.Column(
        db.String(20),
        nullable=False
    )

    tasks = db.relationship(
        "Task",
        backref="subject",
        cascade="all, delete",
        lazy=True
    )


# ---------------- TASK ---------------- #

class Task(db.Model):

    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    task_name = db.Column(
        db.String(150),
        nullable=False
    )

    deadline = db.Column(
        db.Date,
        nullable=False
    )

    estimated_time = db.Column(
        db.Integer,
        nullable=False
    )

    importance = db.Column(
        db.Integer,
        nullable=False
    )

    mandatory = db.Column(
        db.Boolean,
        default=False
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    notes = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return f"<Task {self.task_name}>"