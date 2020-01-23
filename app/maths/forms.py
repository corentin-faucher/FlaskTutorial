from math import pi
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired

class OscillationInputForm(FlaskForm):
	A = FloatField(label='amplitude', description='A', default=1.0, validators=[InputRequired()])
	b = FloatField(label='amort.', description='\\beta', default=0.0, validators=[InputRequired()])
	w = FloatField(label='freq.', description='\\omega', default=2*pi, validators=[InputRequired()])
	T = FloatField(label='période', description='T', default=18, validators=[InputRequired()])

	submit = SubmitField('Faire le graph !')

class JustShowMeTheSolutionForm(FlaskForm):
	redo = SubmitField('Non... un autre.')
	submit = SubmitField('Montre moi juste la solution...')