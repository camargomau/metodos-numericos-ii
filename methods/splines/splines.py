"""
Interpolates a table through splines.
"""

from sympy import expand, plot, solve, Symbol
from .. import input_types
from ..utilities import clear_screen

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

        self.polynomial = expand(
            self.coefficients[a]*(x - spline.points[i][absc])**3 +
            self.coefficients[b]*(x - spline.points[i][absc])**2 +
            self.coefficients[c]*(x - spline.points[i][absc]) +
            self.coefficients[d]
        ).evalf(n=6)
        """The spline as a sympy object."""

        x_sign = "-" if spline.points[i][absc] >= 0 else "+"
        coeff_sign = ["+" if self.coefficients[i]
                      >= 0 else "-"for i in range(0, 4)]

        self.full_expression = (
            f"{round(self.coefficients[a], 6)}(x {x_sign} "
            f"{round(abs(spline.points[i][absc]), 6)})^3 {coeff_sign[b]} "
            f"{round(abs(self.coefficients[b]), 6)}(x {x_sign} "
            f"{round(abs(spline.points[i][absc]), 6)})^2 {coeff_sign[c]} "
            f"{round(abs(self.coefficients[c]), 6)}(x {x_sign} "
            f"{round(abs(spline.points[i][absc]), 6)}) {coeff_sign[d]} "
            f"{round(abs(self.coefficients[d]), 6)}"
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
        self.n = input_types.integer("• ¿Cuántos intervalos tiene la tabla? ")
        """n is the amount of intervals; we have n+1 points."""

        print("\nPara introducir los puntos en la tabla,"
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

    def __str__(self):
        table_string = self.generate_table_string()

        full_splines = [str(spline) for spline in self.splines]
        developed_splines = [str(spline.polynomial) for spline in self.splines]

        full_string, developed_string = "", ""
        for i in range(self.n):
            full_string += (f"\n• g_{i}(x) = {full_splines[i]} "
                            f"en [{self.points[i][absc]}, "
                            f"{self.points[i+1][absc]}]")
            developed_string += (f"\n• g_{i}(x) = "
                                 f"{developed_splines[i].replace('**', '^').replace('*', '')} "
                                 f"en [{self.points[i][absc]}, "
                                 f"{self.points[i+1][absc]}]")

        return (
            f"La tabla introducida fue:"
            f"\n\n{table_string}\n\n"
            f"Los splines que interpolan esta tabla son:"
            f"{full_string}\n\n"
            f"En su forma desarrollada:"
            f"{developed_string}"
        )

    def solve_equations(self):
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

    def generate_splines(self):
        """
        Method that generates the splines based off of
        the results of solving the necessary equations
        """

        self.solve_equations()
        self.splines = [SplinePolynomial(self, i) for i in range(self.n)]

    def interpolate(self):
        """
        Method that interpolates a given value by using the generated splines
        """

        while True:
            value = input_types.real("• ¿Qué valor desea interpolar? ")

            while (value < self.points[0][absc] or
                    value > self.points[self.n][absc]):
                value = input_types.real("-> Introduzca un valor dentro de la tabla: ")

            for i in range(self.n):
                if (value >= self.points[i][absc] and
                        value <= self.points[i+1][absc]):
                    interpolation = self.splines[i].polynomial.evalf(n=6, subs={x: value})

            print(f"-> Interpolando, se obtiene el punto ({value}, {interpolation})")

            another_q = input_types.boolean("\n¿Desea interpolar otro valor? (S/N) ", "S", "N")
            if another_q.upper() == "N":
                break

    def plot(self):
        """
        Method that plots all the generated splines
        """
        polynomials = [spline.polynomial for spline in self.splines]
        ranges = [(x, self.points[i][absc], self.points[i+1][absc])
                  for i in range(self.n)]
        to_plot = tuple(zip(polynomials, ranges))

        plot(*to_plot, title="Splines")

    def generate_table_string(self):
        """
        Method that puts the table into a nicely-formatted string.
        """

        to_print = ""
        header = [["i", "x_i", "f(x_i)", "h_i", "f[x_i, x_i+1]"],
                  ["", "", "", "", "", ""]]
        to_print += ("| {:^3} | {:^9} | {:^9} | {:^9} | {:^13} |"
                     .format(*header[0]))
        to_print += ("\n| {:-^3} | {:-^9} | {:-^9} | {:-^9} | {:-^13} |"
                     .format(*header[1]))

        for i in range(self.n+1):
            row = [i] + [float(p) for p in self.points[i]]

            if i != self.n:
                row += [float(self.h[i])] + [float(self.differences[i])]
                to_print += (
                    "\n| {:^3} | {:< 9.6g} | {:< 9.6g} |"
                    " {:< 9.6g} | {:< 13.6g} |"
                    .format(*row))
            else:
                row += [" N/A"] + [" N/A"]
                to_print += (
                    "\n| {:^3} | {:< 9.10g} | {:< 9.10g} | {:<9} | {:<13} |"
                    .format(*row))

        return to_print


def main():
    print("Método de Splines")
    print("\nEste método consiste en interpolar una tabla de datos mediante"
          "\nsplines: polinomios de tercer grado que aproximan un intervalo"
          "\nde la tabla cada uno.")
    input("\nPresiona cualquier tecla para continuar.")
    clear_screen()

    while True:
        spline = SplineInterpolation()
        spline.generate_splines()
        print(f"\n{spline}\n")

        interpolate_q = input_types.boolean("¿Desea interpolar algún valor? (S/N) ", "S", "N")
        if interpolate_q.upper() == "S":
            spline.interpolate()

        plot_q = input_types.boolean("¿Desea graficar los splines? (S/N) ", "S", "N")
        if plot_q.upper() == "S":
            spline.plot()

        another_q = input_types.boolean("¿Desea interpolar otra tabla con este método? (S/N) ", "S", "N")
        if another_q.upper() == "N":
            break

if __name__ == "__main__":
    main()
