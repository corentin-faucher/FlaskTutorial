from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import matplotlib
import os, time, glob

matplotlib.use('Agg')

def oscillation_amortie(t, A, b, w):
	return A * exp(-b*t) * cos(w*t)

def compute(A, b, w, T, resolution=500):
	""" Retourne le graph d'une oscillation amortie
	come une image html (string simple). """
	t = linspace(0, T, resolution+1)
	u = oscillation_amortie(t, A, b, w)
	plt.figure()
	plt.plot(t, u)
	plt.title(r'A=%g, $\beta=%g$, $\omega=%g$.' % (A, b, w))

	from io import BytesIO
	buffer = BytesIO()
	plt.savefig(buffer, format='png')
	import base64
	data = base64.b64encode(buffer.getbuffer()).decode("ascii")

	return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
	print(compute(1, 0.1, 1, 20))