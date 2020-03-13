# MTH1102, Calcul II
# Chapitre 6
# Intégrale double sur un rectangle.
# Corentin Faucher
# 21 janvier 2020

# Import python
from random import randint
from sympy import Integral, integrate, latex, mathematica_code, Rational, symbols
from sympy.parsing.mathematica import mathematica
# Import personnel
from app.maths.mathutils import latexWrapInPar


class Chap6_intR:
	name = "Intégrale double sur un rectangle"

	def __init__(self):
		# Domaine
		self.a = randint(-10, 9)
		self.b = randint(self.a + 1, 10)
		self.c = randint(-10, 9)
		self.d = randint(self.c + 1, 10)
		# Init de la fonction à intégrer
		x, y = symbols('x,y')
		nb_termes = randint(1, 3)		# Ici, on fait un simple polynôme.
		f = Rational(randint(-5, 5))	# Init comme expression symbolique.
		for i in range(nb_termes):
			f += randint(-5, 5) * x ** randint(0, 2) * y ** randint(0, 2)
		# On ne garde pas l'expression symbolique (trop lourd pour les cookies),
		# on ne garde que l'expression sous forme de string.
		self.f_string = mathematica_code(f)

	def getStatement(self):
		f = mathematica(self.f_string)
		# Rédaction de l'énoncé.
		return '\n'.join([
			r"Évaluez l'intégrale",
			r"\[ J = \iint_R %s \, dA, \]" % latexWrapInPar(f),
			rf"où \( R \) est le rectangle \( R = [{self.a}, {self.b}] \times [{self.c}, {self.d}] \)."
		])

	def getSolution(self):
		# Calculs
		x, y = symbols('x,y')
		f = mathematica(self.f_string)
		a, b, c, d = self.a, self.b, self.c, self.d
		J1 = Integral(Integral(f, (y, c, d)), (x, a, b))
		Ax = integrate(f, (y, c, d))
		J2 = Integral(Ax, (x, a, b))
		J3 = integrate(Ax, (x, a, b))
		J4 = Integral(Integral(f, (x, a, b)), (y, c, d))
		Ay = integrate(f, (x, a, b))
		J5 = Integral(Ay, (y, c, d))
		J6 = integrate(Ay, (y, c, d))
		# Rédaction de la solution
		return '\n'.join([
			r"Selon l'ordre \( dx\, dy \) : ",
			r"\[\renewcommand{\arraystretch}{3.0}\begin{array}{lll}",
			r"J &= &  %s \\" % latex(J4),
			r"  &= &  %s \\" % latex(J5),
			r"  &= &  %s. " % latex(J6),
			r"\end{array}\]",
			r"Selon l'ordre \( dy\, dx \) : ",
			r"\[\renewcommand{\arraystretch}{3.0}\begin{array}{lll}",
			r"J &= &  %s \\" % latex(J1),
			r"  &= &  %s \\" % latex(J2),
			r"  &= &  %s. " % latex(J3),
			r"\end{array}\]",
		])

# Testing de chap6_intD.py
if __name__ == '__main__':
	problem = Chap6_intD()
	problem.setDomain()
	problem.setIntegrand()
	problem.generateStatement()
	problem.generateSolution()
	print(problem.statement)
	print(problem.solution)

