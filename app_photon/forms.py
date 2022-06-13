from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, FileField
from wtforms.validators import DataRequired


class Parsing(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    clone = BooleanField('Clone', default=False) #убрать
    only_urls = BooleanField('Only URLS', default=False)
    keys = BooleanField('Keys', default=False)
    dns = BooleanField('DNS', default=False) #убрать
    download = SubmitField('DOWNLOAD ZIP', default=False)


class DataGenerator(FlaskForm):
    download = SubmitField('DOWNLOAD CSV', default=False)
    n = IntegerField('n', default=2)
    m = IntegerField('m', default=150)


class Image(FlaskForm):
    file = FileField('FILE')
