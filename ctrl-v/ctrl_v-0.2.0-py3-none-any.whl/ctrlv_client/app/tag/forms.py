from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    HiddenField
)
from wtforms.validators import DataRequired, ValidationError, Length, Optional
from ctrlv_client.app.models import Tag
from markupsafe import Markup


class UpdateTagForm(FlaskForm):
    tag_name = StringField('Tag', validators=[DataRequired(), Length(max=255)])
    # https://stackoverflow.com/questions/15988373
    # /how-do-i-add-a-font-awesome-icon-to-input-field
    # https://stackoverflow.com/questions/39147578
    # /set-wtforms-submit-button-to-icon
    update = SubmitField(Markup("&#xf00c;").unescape())
    delete = SubmitField(Markup("&#xf00d;").unescape())
    tag_id = HiddenField()

    def validate_snippet_id(form, field):
        if not Tag.query.filter_by(tag_id=field.data).first():
            raise ValidationError('No such tag!')

    def validate_tag_name(form, field):
        other_tag_names = [
            t.tag_name for t in
            Tag.query.filter(Tag.tag_id != form.tag_id.data).all()
        ]
        if field.data.strip().lower() in other_tag_names:
            raise ValidationError('Name already present!')


class TagFilterForm(FlaskForm):
    search = StringField(
        validators=[
            Optional(strip_whitespace=True),
            Length(max=255)
        ],
        render_kw={"placeholder": "Search tag"}
    )
    btnsubmit = SubmitField('Search')
