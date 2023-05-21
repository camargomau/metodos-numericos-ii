import sympy

def calcular_simpson_un_tercio(x,fx,h):
    n=len(x)
    sum_par=float()
    sum_impar=float()
    for i in range(1,n-1):
        if((i%2)==0):
            sum_par += fx[i]
        else:
            sum_impar += fx[i]
    #Calcula el area total
    area =(h/3)*(fx[0]+fx[n-1]+ 2*sum_par+4*sum_impar)
    area_redondeada=round(area,6)
    return area_redondeada

def calcular_simpson_tres_octacos(x,fx,h):
    n=len(x)
    sum_tres = float()
    suma = float()
    for i in range(1,n-1):
        if((i%3==0)):
            sum_tres += fx[i]
        else:
            suma += fx[i]
    #Calcula el area total
    area=(3/8)*h*(fx[0]+fx[n-1]+2*sum_tres+3*suma)
    area_redondeada=round(area,6)
    return area_redondeada
           

def calcular_h(x):
    n=len(x)
    h=(x[n-1]-x[0])/(n-1)
    return h

def validacion(n):
    opc = int(input("Seleccione la opcion deseada:\n\t1. Simpson 1/3:\n\t2. Simpson 3/8:\n "))
    if(opc==1):
        if(((n-1)%2)==0):
            opcion = 1
            return opcion
        else: 
            print("\nERROR AL ESCOGER LA CANTIDAD DE DATOS...\nPARA SIMPSON 1/3 LA CANTIDAD DE INTERVALOS ENTRE DATOS TIENE QUE SER MULTIPLO DE 2")
    elif(opc==2):
        if(((n-1)%3)==0):
            opcion = 2
            return opcion
        else: 
            print("\nERROR AL ESCOGER LA CANTIDAD DE DATOS...\nPARA SIMPSON 3/8 LA CANTIDAD DE INTERVALOS ENTRE DATOS TIENE QUE SER MULTIPLO DE 3")

def main():
    while True:
        x=[]
        fx=[]
        while True:
            n = int(input("Ingrese la cantidad de datos: "))
            opc=validacion(n)
            if opc==1 or opc==2:
                print(opc)
                break
        for i in range(n):
            if(i==0):
                x.append(float(input(f"Ingrese el valor de a: ")))
                fx.append(float(input(f"Ingrese el valor de f(a): ")))
            elif(i==(n-1)):
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
        #Calculamos h
        h=calcular_h(x)
        #Calculamos el area
        if opc==1:
            area=calcular_simpson_un_tercio(x,fx,h)
        else:
            area=calcular_simpson_tres_octacos(x,fx,h)
        
        print("El área bajo la curva de la tabla dada es: ",area)
        
        repetir = input("¿Desea repetir el programa? (s/n): ")
        if repetir.lower() != 's':
            break


# Iniciar el programa

main()