import eshirlitos

while True :
    try:
        print("#####esport eShirlitos#####")
        print("1.-Registrar puntajes")
        print("2.-listar tods los puntajes")
        print("3.-imprimir por tipo ")
        print("4.-salir del programa")
        direccion=int(input("seleccione una funcion: "))

        if direccion==1:
            while True:
                try:
                    print("seleccione el tipo de juego")
                    print("1.- Valorant")
                    print("2.- Fifa")
                    print("3.- Fornite")
                    opcion=int(input(""))
                    if opcion>4:
                        print(" numero selecionado equivocado, por favor intente de nuevo")
                except:
                    print("numero/palabra erronea, seleccione de nuevo")
    except:
        print("numero/palabra erronea, seleccione de nuevo")
        #elif direccion==3:
        #elif direccion==3:
        #elif direccion==4: