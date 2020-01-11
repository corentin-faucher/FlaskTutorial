from flask import render_template, request, flash
from flask_login import login_required

from app.maths import bp
from app.maths.compute import compute
from app.maths.forms import InputForm


@bp.route('/maths_test', methods=['GET', 'POST'])
@login_required
def maths_test():
	form = InputForm()

	if form.validate_on_submit():
		result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
		flash('Équation mise à jour.')
	else:
		result = None

	return render_template("maths/maths_test.html", form=form, result=result)