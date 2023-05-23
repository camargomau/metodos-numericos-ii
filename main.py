from methods.utilities import clear_screen, portada
from methods.lagrange import lagrange
from methods.hermite import hermite
from methods.splines import splines
from methods.simpson import simpson_13, simpson_38

def menu():
    global eleccion_metodo
    opciones_metodos = {
        1: "Método de Lagrange",
        2: "Método de Hermite",
        3: "Método de Splines",
        4: "Método de Simpson 1/3",
        5: "Método de Simpson 3/8",

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
            clear_screen()
            lagrange.main()
            continue
        elif eleccion_metodo == 2:
            clear_screen()
            hermite.main()
            continue
        elif eleccion_metodo == 3:
            clear_screen()
            splines.main()
            continue
        elif eleccion_metodo == 4:
            clear_screen()
            simpson_13.main()
            continue
        elif eleccion_metodo == 5:
            clear_screen()
            simpson_38.main()
            continue
        elif eleccion_metodo == 0:
            break

if __name__ == "__main__":
    portada()
    menu()
