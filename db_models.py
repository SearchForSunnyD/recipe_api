from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User in the system."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

    user_img = db.Column(
        db.String,
        default="/static/images/default-pic.png",
    )

    password = db.Column(
        db.String,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )


    @classmethod
    def signup(cls, username, password, user_img):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode("UTF-8")

        user = User(
            username=username,
            password=hashed_pwd,
            user_img=user_img,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user

        return None


class Recipe(db.Model):
    """"""

    __tablename__ = "recipes"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String,
        nullable=False,
    )
    uri = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )


class Filter(db.Model):
    __tablename__ = "filters"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String,
        nullable=False,
    )
    value = db.Column(
        db.String,
        nullable=False,
    )
    f_type = db.Column(
        db.Integer,
        db.ForeignKey("filter_types.id", ondelete="cascade"),
        nullable=False,
    )
    type = db.relationship("FilterType", backref="filters")


class FilterType(db.Model):
    __tablename__ = "filter_types"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String,
        nullable=False,
    )
    value = db.Column(
        db.String,
        nullable=False,
    )
