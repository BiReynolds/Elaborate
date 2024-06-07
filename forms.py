from flask_wtf import FlaskForm,CSRFProtect
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class ContentForm(FlaskForm):
    nickname = StringField('Nickname',validators=[DataRequired()])
    html = StringField('html',validators = [DataRequired()])
    submit = SubmitField('Submit')

    