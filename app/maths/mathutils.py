# Petites fonction pratiques pour les problèmes de maths.
# Corentin Faucher
# 21 janvier 2020

from sympy import Add, latex
from random import randint, random
from math import log10, floor
from collections.abc import Iterable

def randsign():
	""" Retourne 1 ou -1 au hasard."""
	return 1 if random() < 0.5 else -1


def randsignint(a, b):
	""" Retourne un entier au hasard entre a et b avec un signe +/- au hasard."""
	return randint(a, b) * (1 if random() < 0.5 else -1)


def randsignintexclude(a, b, to_exclude):
	""" Retourne un entier au hasard entre a et b avec un signe +/- au hasard. 
		S'assure de ne pas être (ou pas dans) "to_exclude"."""
	essai = 0
	while essai < 100:
		to_return = randsignint(a, b)
		if isinstance(to_exclude, Iterable):
			if to_return not in to_exclude:
				return to_return
		else:
			if to_return != to_exclude:
				return to_return
		essai += 1
	print(" Erreur, randsignintexclude. Trop de contraintes... %s" % to_exclude)
	return to_return


def randintexclude(a, b, to_exclude):
	""" Retourne un entier au hasard entre a et b. 
	S'assure de ne pas être (ou pas dans) "to_exclude"."""
	essai = 0
	while essai < 100:
		to_return = randint(a, b)
		if isinstance(to_exclude, Iterable):
			if to_return not in to_exclude:
				return to_return
		else:
			if to_return != to_exclude:
				return to_return
		essai += 1
	print(" Erreur, randsignintexclude. Trop de contraintes... %s" % to_exclude)
	return to_return


def round4(x):
	""" Garde les 4 premiers chiffres significatifs."""
	if abs(x) < 0.00001:
		return 0
	return round(x, -int(floor(log10(abs(x)))) + 3)


def getTermWithPlus(term, not_first):
	if not not_first or term[0] == '-':
		return term
	return " + " + term


def latexWrapInPar(poly):
	""" Convertie l'expression symbolique "poly" en Latex 
	et ajoute des parenthèses s'il y a plusieurs termes."""
	termCount = len(Add.make_args(poly))
	if termCount > 1:
		return r"\left(" + latex(poly) + r"\right)"
	else:
		return latex(poly)


