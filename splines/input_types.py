"""
Provides functions that handle input with various data types.
"""
from sympy import sympify


def integer(prompt):
    """
    Function for handling the input of an integer.
    """

    while True:
        try:
            answer = int(input(prompt))

            if answer < 1:
                raise IndexError

            break
        except IndexError:
            prompt = "-> Introduzca un número entero mayor o igual que 1: "
        except ValueError:
            prompt = "-> Introduzca un número entero: "

    return answer


def real(prompt, size=1, separator=" "):
    """
    Function for handling the input of real numbers (sympy Float/Rational);
    supports a single value or a list of values.
    """

    if size == 1:
        while True:
            try:
                answer = sympify(input(prompt))
                if not answer.is_real:
                    raise ValueError
                break
            except ValueError:
                prompt = "-> Introduzca un número real: "
    else:
        while True:
            answer = input(prompt).strip().split(separator)
            if len(answer) != size:
                prompt = f"-> Introduzca exactamente {size} reales: "
                continue

            try:
                answer = [sympify(i) for i in answer]
                if not all(i.is_real for i in answer):
                    raise ValueError
                break
            except ValueError:
                prompt = "-> Solo inserta números reales: "

    return answer

def boolean(prompt, opt_1, opt_2):
    """
    Function for handling a boolean input;
    opt_1 and opt_2 are single capital letters each
    """
    answer = input(prompt)
    while answer.upper() != opt_1 and answer.upper() != opt_2:
        answer = input(f"-> Introduzca {opt_1} o {opt_2}: ")

    return answer
