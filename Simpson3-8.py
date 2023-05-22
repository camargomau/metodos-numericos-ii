import sympy

def calcular_simpson_tres_octavos(x, fx, h):
    n = len(x)
    sum_tres = float()
    sum_t = ""
    suma = float()
    sum = ""
    for i in range(1, n-1):
        if ((i % 3) == 0):
            sum_tres += fx[i]
            if(i == (n-4)):
                sum_t += str(fx[i])
            else:
                sum_t += str(fx[i])+"+"
        else:
            suma += fx[i]
            if(i == (n-2)):
                sum += str(fx[i])
            else:
                sum += str(fx[i]) + "+"
    # Calcula el área total
    area = ((3*h) / 8) * (fx[0] + fx[n-1] + 2 * sum_tres + 3 * suma)
    a = "((3*"+format(h, ".6f")+") / 8) * (" + str(fx[0])+"+" + str(fx[n-1]) + "+ 2* (" +sum_t+") + 3*(" +sum+")"
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
        if n % 3 != 0:
            print("El número de intervalos ingresado no cumple con la condición (3n).")
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

    area = calcular_simpson_tres_octavos(x, fx, h)

    print("El área bajo la curva de la tabla dada es: ", area)

# Iniciar el programa
main()

