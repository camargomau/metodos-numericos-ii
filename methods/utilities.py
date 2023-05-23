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
             "Lagrange, Hermite, Splines, Simpson\n",
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
