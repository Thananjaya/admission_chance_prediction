from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets.html5 import NumberInput

class AdmissionPredictionForm(FlaskForm):
    print('somthing in the form')
    gre_score = IntegerField(
        'GRE Score', 
        widget=NumberInput(), 
        validators=[DataRequired(), NumberRange(min=260, max=340, message="Should be between 260 and 340")]
    )
    toefl_score = IntegerField(
        'TOEFL Score', 
        widget=NumberInput(), 
        validators=[DataRequired()]
    )
    university_rating = SelectField(
        'University Rating', 
        choices=[('1', 1), ('2', 2), ('3',3), ('4',4), ('5',5)]
    )
    sop = FloatField(
        'Score - Statement of Purpose',
        validators=[DataRequired(), NumberRange(min=1, max=5, message="Should be between 1 and 5, can be in one decimal places")],
        description="Integer field up to decimal point"
    )
    lor = FloatField(
        'Score - Letter of Recommendation', 
        validators=[DataRequired(), NumberRange(min=1, max=5, message="Should be between 1 and 5, can be in one decimal places")],
        description="Integer field up to decimal point"
    )
    cgpa = FloatField(
        'CGPA', 
        validators=[DataRequired(), NumberRange(min=1, max=10, message="Should be between 1 and 10, can be in one decimal places")],
        description="Integer field up to decimal point"
    )
    research = SelectField(
        'Any Reseach Activity', 
        choices=[('1', 'Yes'), ('0', 'No')]
    )
    submit = SubmitField('Predict')