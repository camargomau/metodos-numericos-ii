"""
Interpolates a table through splines.
"""

from sympy import expand, solve, Symbol, pretty, evaluate, Abs
import input_types

absc, ord = 0, 1
a, b, c, d = 0, 1, 2, 3
x = Symbol("x")


class SplinePolynomial:
    """
    Class that contains a given spline.
    """

    def __init__(self, spline, i):
        self.coefficients = [0, 0, 0, 0]
        """Contains the coefficients of the spline's polynomial."""
        self.coefficients[a] = (spline.s[i+1] - spline.s[i])/(6 * spline.h[i])
        self.coefficients[b] = spline.s[i]/2
        self.coefficients[c] = spline.differences[i] - \
            ((spline.s[i+1] + 2*spline.s[i])/6)*spline.h[i]
        self.coefficients[d] = spline.points[i][ord]

        self.polynomial = evaluate(
            self.coefficients[a]*(x - spline.points[i][absc])**3 +
            self.coefficients[b]*(x - spline.points[i][absc])**2 +
            self.coefficients[c]*(x - spline.points[i][absc]) +
            self.coefficients[d]
        )
        """The spline as a sympy object."""

        x_sign = "-" if spline.points[i][absc] >= 0 else "+"
        coeff_sign = ["+" if self.coefficients[i] >= 0 else "-" for i in range(0, 4)]

        self.full_expression = (
            f"{float(self.coefficients[a])}(x {x_sign} {abs(spline.points[i][absc])})^3 {coeff_sign[b]} "
            f"{abs(self.coefficients[b])}(x {x_sign} {abs(spline.points[i][absc])})^2 {coeff_sign[c]} "
            f"{abs(self.coefficients[c])}(x {x_sign} {abs(spline.points[i][absc])}) {coeff_sign[d]} "
            f"{abs(self.coefficients[d])}"
        )
        """The spline's polynomial in its full non-developed form."""

    def __str__(self):
        return self.full_expression


class SplineInterpolation:
    """
    Class that contains the table, the splines and other relevant values,
    as well as the methods that do all the work.
    """

    def __init__(self):
        self.n = input_types.integer("¿Cuántos intervalos tiene la tabla? ")
        """n is the amount of intervals; we have n+1 points."""

        print("Para introducir los puntos en la tabla,"
              " siga el formato \"x f(x)\":")
        self.points = [input_types.real(
            f"• Punto {i}: ", 2) for i in range(self.n+1)]
        """All the points that are to be interpolated;
        list of lists of the form (x, f(x))."""

        self.h = [self.points[i+1][absc] - self.points[i][absc]
                  for i in range(self.n)]
        """List of every interval's size"""
        self.differences = [(self.points[i+1][ord] - self.points[i][ord]) /
                            (self.points[i+1][absc] - self.points[i][absc])
                            for i in range(self.n)]
        """List of every interval's finite difference"""

        self.s = []
        """List of every S value;
        these are used to calculate the splines' polynomials"""
        self.splines = []
        """List of every spline as a SplinePolynomial"""
        self.symb = []
        """List of every S symbol (s0, s1, etc.);
        only used for telling sympy to solve
        for these values in the equations"""
        self.equations_to_solve = []
        """List of every equation that's to be solved"""

    def equations(self):
        """
        Method that generates the equations we have to solve
        to get the coefficients of every spline, then solves them;
        the end result is the population of the s list
        """

        self.symb = [Symbol(f"s{i}") for i in range(self.n+1)]
        self.equations_to_solve = [
            self.symb[i]
            if (i == 0 or i == self.n)
            else (self.symb[i-1]*self.h[i-1]
                  + 2*self.symb[i]*(self.h[i-1]+self.h[i])
                  + self.symb[i+1]*self.h[i]
                  - 6*(self.differences[i]-self.differences[i-1]))
            for i in range(self.n+1)
        ]

        self.s = list(solve(self.equations_to_solve, self.symb,
                      dict=True)[0].values())

    def polynomials(self):
        """
        Method that generates the splines based off of
        the results of solving the necessary equations
        """
        self.equations()
        self.splines = [SplinePolynomial(self, i) for i in range(self.n)]

    def print_table(self):
        encabezado = [["i", "x_i", "f(x_i)", "h_i", "f[x_i, x_i+1]"],
                      ["", "", "", "", "", ""]]

        print("| {:^3} | {:^9} | {:^9} | {:^9} | {:^13} |".format(
            *encabezado[0]))
        print(
            "| {:-^3} | {:-^9} | {:-^9} | {:-^9} | {:-^13} |"
            .format(*encabezado[1]))

        for i in range(self.n+1):
            row = [i] + [float(p) for p in self.points[i]]

            if i != self.n:
                row += [float(self.h[i])] + [float(self.differences[i])]
                print(
                    "| {:^3} | {:< 9.6g} | {:< 9.6g} |"
                    " {:< 9.6g} | {:< 13.6g} |"
                    .format(*row))
            else:
                row += [" N/A"] + [" N/A"]
                print(
                    "| {:^3} | {:< 9.10g} | {:< 9.10g} | {:<9} | {:<13} |"
                    .format(*row))


test = SplineInterpolation()
test.polynomials()
test.print_table()
print(test.splines[0])
