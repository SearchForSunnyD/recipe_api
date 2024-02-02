from flask_wtf import FlaskForm
from db_models import Filter, FilterType
from wtforms import (
    StringField,
    PasswordField,
    SelectMultipleField,
    widgets,
    SearchField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length, NumberRange


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])
    user_img = StringField("(Optional) Image URL")


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class FilterForm(FlaskForm):
    """A form for the query filtering"""

    q = SearchField("Search")
    submit = SubmitField("Submit")


def build_filters():
    """Generate the filter fields from the database dynamically"""
    filter_types = FilterType.query.all()

    filter_options = {
        ftype.value: [
            (f.value, f.name) for f in Filter.query.filter_by(f_type=ftype.id).all()
        ]
        for ftype in filter_types
    }
    for field_name, choices in filter_options.items():
        setattr(
            FilterForm,
            field_name,
            MultiCheckboxField(field_name, choices=choices),
        )
