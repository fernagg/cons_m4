from vehiculo import *

while True:
    try:
        print("Sistema de Control de Vehículos en Peaje")
        print("-------------MENÚ-------------")
        print("1.- Ingresar vehículos manualmente y mostrarlos por pantalla")
        print("2.- Agregar vehículos de todo tipo automaticamente y mostrar información por pantalla ")
        print("3.- Agregar vehículos desde archivo y mostrar información por pantalla")
        print("4.- Salir")   
        opcion = int(input("Ingrese su opción: "))
        if opcion < 1 :
            print("Opción no válida")
        else:
            break
    except ValueError:
        print("Opción no válida")

    if (opcion == 1):
        while True:
            try:
                opcion = int(input("Ingrese la cantidad de vehículos que desea ingresar: "))
                if opcion<1:
                    print("Numero debe ser entero positivo")
                else:
                    break
            except ValueError:
                print("Dato ingresado no válido")

        vehiculos = []
        for i in range(opcion):
            while True:
                try:
                    print("\nDatos del vehículo ", i+1)
                    marca = input("Inserte la marca del automóvil: ")
                    modelo = input("Inserte el modelo: ")
                    num_ruedas = int(input("Inserte el número de ruedas: "))
                    velocidad = int(input("Inserte la velocidad en km/h: "))
                    cilindrada = int(input("Inserte el cilindraje en cc: "))
                    vehiculos.append(Automovil(marca, modelo, num_ruedas, velocidad, cilindrada))
                    break
                except ValueError as error:
                    print(error)       
        if opcion>0:
            print("\nImprimiendo por pantalla los Vehículos:\n")
            for i in range(opcion):
                print(f"Datos del vehículo {i+1} : {vehiculos[i]} ")
            print("\n\n")
    
    elif opcion==2:
        
        particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
        carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
        bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
        motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
        print(particular)
        print(carga)
        print(bicicleta)
        print(motocicleta)
        print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta,Vehiculo)}")
        print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta,Automovil)}")
        print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta,Particular)}") 
        print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(motocicleta,Carga)}")
        print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta,Bicicleta)}")
        print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta,Motocicleta)}")
    elif opcion==3:
        particular = Particular("Ford", "Fiesta", 4, "180", "500", "5")
        carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
        bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
        motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
        lista_vehiculos=[]
        lista_vehiculos+=[particular,carga,bicicleta,motocicleta]
        guardar_csv(lista_vehiculos)
        leer_datos_csv()

    elif opcion==4:
        print("Adiós")
        break
    else:
        print("Ingrese una opción correcta\n")