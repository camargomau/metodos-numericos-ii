import hermite.hermite as hermite
import splines.splines as splines

def clear_screen():
    import os
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def portada():
    clear_screen()
    datos = ["Universidad Nacional Autónoma de México",
             "Facultad de Estudios Superiores Acatlán",
             "Matemáticas Aplicadas y Computación\n",
             "{:-^47}\n".format(""),
             "Proyecto Final",
             "Lagrange, Newton, Hermite, Splines, Simpson\n",
             "Burciaga Piña Erick Osvaldo",
             "Camargo Badillo Luis Mauricio",
			 "Gudiño Romero Miguel Ángel",
			 "Gutiérrez Flores Daniel\n",
             "Métodos Numéricos II",
             "Grupo 2402\n",
             "{:-^47}\n".format(""),
             "Presiona enter para continuar"]

    for dato in datos:
        print(" {:^47} ".format(dato))

    input()
    clear_screen()

def menu():
    global eleccion_metodo
    opciones_metodos = {
        1: "Método de Lagrange",
        2: "Método de Newton",
        3: "Método de Hermite",
        4: "Método de Splines",
        5: "Métodos de Simpson",

        0: "Salir"
    }

    while True:
        clear_screen()
        print("Métodos disponibles:\n")
        for opcion in opciones_metodos.keys():
            print(f"{opcion} --- {opciones_metodos[opcion]}")

        while True:
            try:
                eleccion_metodo = int(input("\n¿Qué método desea utilizar? "))
            except:
                print("\nIntroduzca un número entero.")
                continue

            if (eleccion_metodo >= 0) and (eleccion_metodo < len(opciones_metodos.keys())):
                break
            else:
                print(
                    f"\nIntroduzca un número entre 0 y {len(opciones_metodos.keys())-1}.")

        if eleccion_metodo == 1:
            input("Método de Lagrange: PENDIENTE")
            continue
        elif eleccion_metodo == 2:
            input("Método de Newton: PENDIENTE")
            continue
        elif eleccion_metodo == 3:
            clear_screen()
            hermite.main()
            continue
        elif eleccion_metodo == 4:
            clear_screen()
            splines.main()
            continue
        elif eleccion_metodo == 5:
            input("Métodos de Simpson: PENDIENTE")
        elif eleccion_metodo == 0:
            break

if __name__ == "__main__":
    portada()
    menu()
