import csv

class ErrorNumero(Exception):
	pass

class Vehiculo:
    
    def __init__(self, marca, modelo, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
    
    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas"

    def atributos(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.ruedas} ruedas"
    
    def atributos2(self):
        pass

class Automovil(Vehiculo):

    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def atributos(self):
        return f"{super().atributos()}, {self.velocidad} km/h, {self.cilindrada} cc"
        #print(super().atributos(), self.velocidad, self.cilindrada) 
    
    def __str__(self):
        return f"{super().atributos()}, {self.velocidad} km/h, {self.cilindrada} cc"

#vehiculo1 = Vehiculo("zuzuki", "swift", 4)
#vehiculo2 = Vehiculo("toyota", "yaris", 4)
#vehiculo3 = Vehiculo("zuzuki", "gixxer", 2)
#auto1 = Automovil("Chevrolet", "Corsa", 4, 140, 1.6)

#vehiculo1.atributos()
#print(auto1.atributos())
#print(vehiculo1)

class Particular(Automovil):

    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.puestos = puestos
    
    def __str__(self):
        return f"{super().atributos()}, Puestos: {self.puestos}"

class Carga(Automovil):

    def __init__(self, marca, modelo, ruedas, velocidad, cilindrada, cap_carga):
        super().__init__(marca, modelo, ruedas, velocidad, cilindrada)
        self.cap_carga = cap_carga

    def __str__(self):
        return f"{super().atributos()}, Carga: {self.cap_carga} Kg"

class Bicicleta(Vehiculo):

    def __init__(self, marca, modelo, ruedas, tipo):
        super().__init__(marca, modelo, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f"{super().atributos()}, Tipo: {self.tipo}"


class Motocicleta(Bicicleta):

    def __init__(self, marca, modelo, ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
    
    def __str__(self):
        return f"{super().atributos()}, Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"


def guardar_csv(lista_vehiculos):
    try:
        with open("vehiculos.csv", "w", encoding="utf-8", newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            for vehiculo in lista_vehiculos:
                vehiculo1 = [(vehiculo.__class__, vehiculo.__dict__)]
                archivo_csv.writerows(vehiculo1)
        
    except Exception as error:
        print(f"Error al guardar los datos: {error}")

def leer_datos_csv():
    try:
        with open("vehiculos.csv", "r") as archivo:
            lista_paticulares=[]
            lista_carga=[]
            lista_bicicletas=[]
            lista_motocicletas=[]
            archivo_csv = csv.reader(archivo)            
            for vehiculo in archivo_csv:
                clase_vehiculo = vehiculo[0]
                vehiculo1 = vehiculo[1]
                if "Particular" in clase_vehiculo:
                    lista_paticulares.append(vehiculo1)
                elif "Carga" in clase_vehiculo:
                    lista_carga.append(vehiculo1)
                elif "Bicicleta" in clase_vehiculo:
                    lista_bicicletas.append(vehiculo1)
                elif "Motocicleta" in clase_vehiculo:
                    lista_motocicletas.append(vehiculo1) 
            
        if len(lista_paticulares) > 0:
            print("Lista de Vehículos Particular")
            for vehiculo in lista_paticulares:
                print(vehiculo)
        if len(lista_carga) > 0:
            print("\nLista de Vehículos Carga")
            for vehiculo in lista_carga:
                print(vehiculo)
        if len(lista_bicicletas) > 0:
            print("\nLista de Vehículos Bicicleta")
            for vehiculo in lista_bicicletas:
                print(vehiculo)
        if len(lista_motocicletas) > 0:
            print("\nLista de Vehículos Motocicleta")
            for vehiculo in lista_motocicletas:
                print(vehiculo)
                

    except FileNotFoundError:
        print("El archivo vehiculos.csv no se encontró.")
    except Exception as error:
        print(f"Error al leer los datos: {error}")