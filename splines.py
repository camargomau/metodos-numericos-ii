"""
Interpolates a table through splines.
"""

from sympy import sympify, Symbol, solve
import input_types

x, y = 0, 1


class SplinePolynomial:
    coefficients = [0 for _ in range(4)]
    full_form = sympify(0)
    simplified_form = sympify(0)


class SplineInterpolation:
    """
    Class that contains the table, the splines and other relevant values,
    as well as the methods that do all the work.
    """

    n = int()
    """n is the amount of intervals; we have n+1 points."""
    points = []

    h = []
    differences = []

    s = []
    splines = []

    symbols = []
    equations_to_solve = []

    def __init__(self):
        self.n = input_types.integer("¿Cuántos intervalos tiene la tabla? ")

        print("Para introducir los puntos en la tabla,"
              " siga el formato \"x f(x)\":")
        self.points = [input_types.real(
            f"• Punto {i}: ", 2) for i in range(self.n+1)]

        self.h = [self.points[i+1][x] - self.points[i][x]
                  for i in range(self.n)]
        self.differences = [(self.points[i+1][y] - self.points[i][y]) /
                            (self.points[i+1][x] - self.points[i][x])
                            for i in range(self.n)]

    def equations(self):
        """
        Method that generates the equations we have to solve
        to get the coefficients of every spline, then solves them;
        the end result is the population of the s list
        """
        self.symbols = [Symbol(f"s{i}") for i in range(self.n+1)]
        self.equations_to_solve = [
            sympify(f"s{i}") if (i == 0 or i == self.n) else sympify(
                f"""s{i-1}*{self.h[i-1]} + 2*s{i}*{self.h[i-1]+self.h[i]}
                + s{i+1}*{self.h[i]}
                - 6*{self.differences[i]-self.differences[i-1]}""")
            for i in range(self.n+1)
        ]

        self.s = list(solve(self.equations_to_solve, self.symbols,
                      dict=True)[0].values())

        print(self.points)
        print(self.h)
        print(self.differences)
        print(self.s)
        print(self.symbols)
        print(self.equations_to_solve)
        print(self.s)


test = SplineInterpolation()
test.equations()
