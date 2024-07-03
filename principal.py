datos=[]
import csv
import os
import time
os.system('cls')
while True:
    os.system('cls')
    print("\tbienvenido al distribuidor de gas Gaxplosive")
    print("cual de las sigientes opciones desea escojer ")
    print("opcion 1°. registrar pedido")
    print("opcion 2°. lista de todos los pedidos")
    print("opcion 3°. buscar pedido mediante Rut")
    print("opcion 4°. imprimir hoja de ruta")
    print("opcion 5°. salir")
    opc=int(input("ingrece opcion: "))
    if opc==1:
        rut=int(input("ingrece su rut sin digito verificador: "))
        nom=input("ingrese su nombre: ")
        print("el precio unitario de un cilindro chico es de 12.500$ pesos")
        cilindro_c=int(input("ingrece la cantidad de cilindros chicos a comprar: "))
        prec_c= cilindro_c *12500
        print("el precio unitario de un cilindro grande es de 25.500$ pesos")
        cilindro_g=int(input("ingrece la cantidad de cilindros grandes a comprar: "))
        prec_g= cilindro_g*25500
        print("comunas a las cuales distribuimos:\n colina\n santiago\n pirque ")
        #com= comuna
        com=input("ingrese una de las comunas antes presentadas: ")
        dire=input("ingrese su direccion: ")
        total=prec_c+prec_g
        str=dato={"rut":rut,"nombre":nom,"comuna":com,"direcion":dire,"cantidad de cilindros chicos":cilindro_c,"cantidad de cilindros grandes":cilindro_g, "total":total}
        datos.append(dato)
    elif opc==2:
        if not datos:
            print("no existen datos registrados")
            time.sleep(2.5)
        else:
            print("los datos son los sigientes")
            print(datos)
            time.sleep(4)
    elif opc==3:
        if not datos:
            print("no existen datos registrados")
            time.sleep(2)
        else:
            buscar_rut=int(input("ingrese el rut a buscar sin digito verificador: "))
            if buscar_rut == rut:
                datos.count(buscar_rut)
                print("los datos buscados son: ",datos)
                time.sleep(4)
            else:
                print("no existe datos asignados a este rut")
                time.sleep(3)
    elif opc==4:
        nom_archivo=input("ingrese el nombre del archivo a guardar: ")
        with open(nom_archivo,mode='x',newline='') as archivo:
            escritor_csv=csv.DictWriter (archivo ,csv,fieldnames=datos)
            escritor_csv.writeheader("colina","santiago","pirque")
            escritor_csv.writerow(datos)
    else:
        print("gracias a Dios")
        time.sleep(2)
        break