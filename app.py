"""
Web application using Flask for a recipe sharing platform.
"""

from flask import Flask, redirect, render_template, url_for, session, request, flash, g
from db_models import db, connect_db, User
from models import Handler
from sqlalchemy.exc import IntegrityError
from forms import UserAddForm, LoginForm, FilterForm, build_filters

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///recipe_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)
with app.app_context():
    db.create_all()
    build_filters()

app.config["SECRET_KEY"] = "I'LL NEVER TELL!!"

CURR_USER_KEY = "curr_user"

handler = Handler()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 page."""
    return render_template("404.html"), 404


@app.route("/")
def show_home():
    """
    Display the home page.
    """
    return render_template("home.html")


##############################################################################
# User routes:


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                user_img=form.user_img.data or User.user_img.default.arg,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", "danger")
            return render_template("signup.html", form=form)

        do_login(user)

        return redirect(url_for("show_home"))

    else:
        return render_template("signup.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect(url_for("show_home"))

        flash("Invalid credentials.", "danger")

    return render_template("login.html", form=form)


def login_required(view):
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            flash("Access unauthorized.", "danger")
            return redirect(url_for("homepage"))
        return view(*args, **kwargs)

    return wrapped_view


def do_login(user):
    """Log in user."""
    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@login_required
@app.route("/logout")
def logout():
    """Handle logout of user."""
    do_logout()
    flash(f"Goodbye!", "success")
    return redirect(url_for("login"))



##############################################################################
# Search Handler


@app.route("/search", methods=["GET", "POST"])
def search():
    """
    Handle recipe search.

    Display search results based on user input and filter options.
    """
    form = FilterForm()

    try:
        query = request.form.get("q")

        if form.validate_on_submit():
            args = [
                {item: value}
                for item, value in form.data.items()
                if value is not None
                and (isinstance(value, list) and value != [])
                and item != "csrf_token"
            ]

        else:
            args = {}

        is_true = handler.api_query(args, q=query)

        if not is_true:
            raise

        return render_template(
            "search_results.html", form=form, query=query, results=handler
        )
    except:
        return render_template("search_results.html", form=form)


@app.route("/next")
def next_page():
    handler.next_page

    return render_template(
        "recipe_card.html",
        results=handler,
    )


@app.route("/recipe/<int:id>")
def show_recipe(id):
    handler.api_uri_query(id)
    try:
        return render_template("recipe_page.html", results=handler.recipe)
    except:
        return 404
