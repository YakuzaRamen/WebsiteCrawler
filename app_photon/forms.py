from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Parsing(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    clone = BooleanField('Clone')
    only_urls = BooleanField('Only URLS')
    keys = BooleanField('Keys')
    dns = BooleanField('DNS')
    submit = SubmitField('SUBMIT')
    download = SubmitField('DOWNLOAD ZIP')
