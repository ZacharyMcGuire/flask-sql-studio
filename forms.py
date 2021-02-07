from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    sql = TextAreaField(u'sql', validators=[DataRequired()])
