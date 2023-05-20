from input import Input
from sympy import sympify
x, y = 0, 1

class SplinePolynomial:
	coefficients = [0 for _ in range(4)]
	full_form = sympify(0)
	simplified_form = sympify(0)

class Splines:
	# n es el número de intervalos; n+1 puntos
	n = int()
	points = list()

	h = list()
	differences = list()

	s = list() 
	polynomials = list()

	equations_to_solve = list()

	def __init__(self):
		self.n = Input.int("¿Cuántos intervalos tiene la tabla? ")

		self.points = [[0 for _ in range(2)] for _ in range(self.n+1)]

		self.h = [0 for _ in range(self.n)]
		self.differences = [0 for _ in range(self.n)]

		self.s = [0 for _ in range(self.n)]
		self.polynomials = [0 for _ in range(self.n)]

		self.equations_to_solve	= [0 for _ in range(self.n+1)]

		print("Para introducir los puntos en la tabla, siga el formato x,f(x):")
		for i in range(self.n+1):
			self.points[i] = Input.real(f"• Punto {i}: ", 2)

		for i in range(self.n):
			self.h[i] = self.points[i+1][x] - self.points[i][x]
			self.differences[i] = (self.points[i+1][y] - self.points[i][y])/(self.points[i+1][x] - self.points[i][x])

	def solve(self):
		for i in range(self.n+1):
			if i == 0 or i == self.n:
				self.equations_to_solve[i] = sympify(f"s{i}")
			else:
				self.equations_to_solve[i] = f"s{i-1}*{self.h[i-1]} + 2*s{i}*{self.h[i-1]+self.h[i]} + s{i+1}*{self.h[i] - 6*{self.differences[i]-self.differences[i-1]}}"

		print(self.points)
		print(self.h)
		print(self.differences)
		print(self.s)
		print(self.equations_to_solve)

test = Splines()
test.solve()
