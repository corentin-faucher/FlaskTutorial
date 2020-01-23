from flask import render_template, request, flash, session
from flask_login import login_required
import jsonpickle

from app.maths import bp
from app.maths.compute import compute
from app.maths.chap6_intD import Chap6_intD
from app.maths.forms import JustShowMeTheSolutionForm, OscillationInputForm


@bp.route('/maths_test', methods=['GET', 'POST'])
@login_required
def maths_test():
	form = OscillationInputForm()

	if form.validate_on_submit():
		result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
		flash('Équation mise à jour.')
	else:
		result = None

	return render_template("maths/maths_test.html", form=form, result=result)

@bp.route('/chap6_intD', methods=['GET', 'POST'])
@login_required
def chap6_intD():
	form = JustShowMeTheSolutionForm()

	print(f"""request.method: {request.method}, form.validate_on_submit: {form.validate_on_submit()},
		form.redo.data: {form.redo.data}, form.submit.data: {form.submit.data}""")


	if request.method == 'POST' and form.validate_on_submit() and form.submit.data:
		problem = jsonpickle.decode(session['problem'])
		statement = problem.getStatement()
		solution = problem.getSolution()
		flash('Solution générée.')
	else:
		problem = Chap6_intD()
		statement = problem.getStatement()
		solution = None
		session['problem'] = jsonpickle.encode(problem)
		print(session['problem'])
		flash('Énoncé généré.')

	return render_template("maths/maths_problem.html", form=form, 
		name=problem.name, statement=statement, solution=solution)


