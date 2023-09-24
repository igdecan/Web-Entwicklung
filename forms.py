from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, HiddenField, SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length

class CreateTodoForm(FlaskForm):
    description = StringField(validators=[InputRequired(), Length(min=5)])
    submit = SubmitField('Create')

class TodoForm(FlaskForm):
    method = HiddenField()
    id = HiddenField()
    complete = BooleanField()
    description = StringField(validators=[InputRequired()])
    list_id = SelectField(coerce=int, choices=[], validate_choice=False)
    submit = SubmitField('Update')