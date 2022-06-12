from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Parsing(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    clone = BooleanField('Clone', default=False) #убрать
    only_urls = BooleanField('Only URLS', default=False)
    keys = BooleanField('Keys', default=False)
    dns = BooleanField('DNS', default=False) #убрать
    download = SubmitField('DOWNLOAD ZIP', default=False)
