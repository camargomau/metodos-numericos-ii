import sympy


def calcular_polinomio_interpolador_lagrange(x, fx):
    polinomio_sin_simplificar = ""
    polinomio_simplificado = ""
    n = len(x)

    # Crear el símbolo x
    x_sym = sympy.symbols('x')

    polinomios_lagrange = []

    for i in range(n):
        polinomio_lagrange = ""

        for j in range(n):
            if j != i:
                polinomio_lagrange += f"({x_sym} - {x[j]}) / ({x[i]} - {x[j]})*"

        polinomios_lagrange.append(polinomio_lagrange + f"{fx[i]}")

    polinomio_sin_simplificar = "+".join(polinomios_lagrange)
    polinomio_simplificado = sympy.simplify(polinomio_sin_simplificar)

    print(polinomio_sin_simplificar)

    return polinomio_simplificado

def interpolar_valor(polinomio_simplificado):
    x = sympy.symbols('x')
    valor = float(input("Ingrese el valor a interpolar: "))
    resultado = polinomio_simplificado.subs(x, valor)
    resultado_redondeado = round(resultado, 6)
    return resultado_redondeado


def main():
    while True:
        n = int(input("Ingrese la cantidad de datos: "))
        x = []
        fx = []

        for i in range(n):
            x.append(float(input(f"Ingrese el valor de x{i}: ")))
            fx.append(float(input(f"Ingrese el valor de f(x{i}): ")))

        # Crear la tabla con valores redondeados a 6 decimales
        header = ["x", "fx"]

        table = [header]
        for row in zip(x, fx):
            rounded_row = [round(cell, 6) if isinstance(cell, float) else cell for cell in row]
            table.append(rounded_row)

        # Imprimir la tabla con columnas alineadas
        column_lengths = [max(len(str(cell)) for cell in column) for column in zip(*table)]
        for row in table:
            formatted_row = [str(cell).ljust(column_length) for cell, column_length in zip(row, column_lengths)]
            print("  ".join(formatted_row))

        # Obtener el polinomio interpolador de Lagrange
        polinomio_simplificado = calcular_polinomio_interpolador_lagrange(x, fx)
        print("Polinomio interpolador de Lagrange simplificado:")
        print(polinomio_simplificado)

        while True:
            interpolar = input("¿Desea interpolar un valor? (s/n): ")
            if interpolar.lower() == 's':
                resultado = interpolar_valor(polinomio_simplificado)
                print(f"El resultado de la interpolación es: {resultado:.6f}")
            else:
                break

        repetir = input("¿Desea repetir el programa? (s/n): ")
        if repetir.lower() != 's':
            break

# Iniciar el programa
main()
