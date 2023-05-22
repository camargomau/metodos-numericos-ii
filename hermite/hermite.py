import sympy

def calcular_polinomio_interpolador_hermite(z, fz, difs):
    polinomio = ""
    n = len(z)

    for k in range(n):
        if k == 0:
            polinomio += str(round(fz[k], 6))
        else:
            polinomio += " + "
            for i in range(k):
                polinomio += f"(x - {round(z[i], 6)})*"
            polinomio += f"({round(difs[k - 1][0], 6)})"
    return polinomio

def simplificar_polinomio(polinomio):
    x = sympy.symbols('x')
    polinomio_simplificado = sympy.simplify(polinomio)
    polinomio_simplificado_rounded = polinomio_simplificado.evalf(n=6)

    return polinomio_simplificado_rounded

def interpolar_valor(polinomio):
    x = sympy.symbols('x')
    valor = float(input("Ingrese el valor a interpolar: "))
    polinomio_funcion = sympy.sympify(polinomio)
    valor_interpolar = polinomio_funcion.subs(x, valor).evalf(n=6)
    return valor_interpolar


def reiniciar_programa():
    reiniciar = input("¿Desea reiniciar el programa? (s/n): ")
    if reiniciar.lower() == "s":
        main()
    else:
        print("Programa finalizado.")

def main():
    print("Método de Hermite")

    n = int(input("Ingrese la cantidad de datos: "))
    x = []
    fx = []
    dfx = []

    for i in range(n):
        x.append(float(input(f"Ingrese el valor de x{i}: ")))
        fx.append(float(input(f"Ingrese el valor de f(x{i}): ")))
        dfx.append(float(input(f"Ingrese el valor de f'(x{i}): ")))

    z = []
    fz = []
    dfz = []
    for i in range(n):
        z.append(x[i])
        z.append(x[i])
        fz.append(fx[i])
        fz.append(fx[i])
        dfz.append(dfx[i])
        dfz.append(dfx[i])

    dif1 = []
    m = 2*n
    difs = []
    for i in range(m-1):
        dif = []
        difs.append(dif)

    for i in range(m-1):
        for j in range(m-1-i):
            if i == 0:
                if fz[j+1]-fz[j] == 0:
                    difs[i].append(dfz[j])
                else:
                    difs[i].append((fz[j+1]-fz[j])/(z[j+1]-z[j]))
            else:
                difs[i].append((difs[i-1][j+1]-difs[i-1][j])/(z[j+i+1]-z[j]))

    max_length = max(len(z), len(fz))
    for i in range(m - 1):
        difs[i].extend(["-"] * (max_length - len(difs[i])))

    # Crear la tabla con valores redondeados a 6 decimales
    header = ["z", "fz"]
    for i in range(m - 1):
        header.append(f"dif{i+1}")

    table = [header]
    for row in zip(z, fz, *difs):
        rounded_row = [round(cell, 6) if isinstance(cell, float) else cell for cell in row]
        table.append(rounded_row)

    # Imprimir la tabla con columnas alineadas
    column_lengths = [max(len(str(cell)) for cell in column) for column in zip(*table)]
    for row in table:
        formatted_row = [str(cell).ljust(column_length) for cell, column_length in zip(row, column_lengths)]
        print("  ".join(formatted_row))

    # Obtener el polinomio interpolador de Hermite
    polinomio = calcular_polinomio_interpolador_hermite(z, fz, difs)

    # Imprimir el polinomio interpolador
    print("Polinomio interpolador de Hermite:")
    print(polinomio)

    # Simplificar el polinomio interpolador
    polinomio_simplificado = simplificar_polinomio(polinomio)
    print("Polinomio interpolador de Hermite (simplificado a mínima expresión con 6 decimales):")
    print(polinomio_simplificado)

    # Interpolar valores
    while True:
        interpolar = input("¿Desea interpolar un valor en el polinomio? (s/n): ")
        if interpolar.lower() == "s":
            valor_interpolar = interpolar_valor(polinomio_simplificado)
            print(f"El valor interpolar es: {valor_interpolar}")
        else:
            break

    reiniciar_programa()

# Iniciar el programa
if __name__ == "__main__":
    main()
