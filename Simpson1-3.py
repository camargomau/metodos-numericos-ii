import sympy

def calcular_simpson_un_tercio(x, fx, h):
    n = len(x)
    sum_par = float()
    sum_p = ""
    sum_impar = float()
    sum_i = ""
    for i in range(1, n-1):
        if ((i % 2) == 0):
            sum_par += fx[i]
            if(i == (n-2)):
                sum_p += str(fx[i])
            else:
                sum_p += str(fx[i])+"+"
        else:
            sum_impar += fx[i]
            if(i == (n-1)):
                sum_i += str(fx[i])
            else:
                sum_i += str(fx[i]) + "+"
    # Calcula el área total
    area = (h / 3) * (fx[0] + fx[n-1] + 2 * sum_par + 4 * sum_impar)
    a = "("+format(h, ".6f")+" / 3) * (" + str(fx[0])+"+" + str(fx[n-1]) + "+ 2* (" +sum_p+") + 4*(" +sum_i+")"
    print(a)
    area_redondeada = round(area, 6)
    return area_redondeada

def calcular_h(x):
    n = len(x)
    h = float(format((x[n-1] - x[0]) / (n-1), ".6f"))
    print(f"El valor de h es: {h}")
    return h

def main():
    x = []
    fx = []

    # Validación del número n
    while True:
        n = int(input("Ingrese la cantidad de intervalos: "))
        if n % 2 != 0:
            print("El número de intervalos ingresado no cumple con la condición (2n).")
            respuesta = input("¿Desea ingresar otro valor? (s/n): ")
            if respuesta.lower() != 's':
                return
        else:
            break

    for i in range(n+1):
        if (i == 0):
            x.append(float(input(f"Ingrese el valor de a: ")))
            fx.append(float(input(f"Ingrese el valor de f(a): ")))
        elif (i == (n)):
            x.append(float(input(f"Ingrese el valor de b: ")))
            fx.append(float(input(f"Ingrese el valor de f(b): ")))
        else:
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

    # Calculamos h
    h = calcular_h(x)

    area = calcular_simpson_un_tercio(x, fx, h)

    print("El área bajo la curva de la tabla dada es: ", area)

# Iniciar el programa
main()
