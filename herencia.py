class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \n Año: {self.anio}")
    
    def avanzar(self):
        pass
    
    def detener(self):
        pass
    
class Carro(Vehiculo):
    def __init__(self, marca, modelo, anio, color):
        super().__init__(marca, modelo, anio)
        self.color = color
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color: {self.color}")
    
    def avanzar(self):
        print("El carro avanza...")
    
    def detener(self):
        print("El carro se detiene...")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, llantas):
        super().__init__(marca, modelo, anio)
        self.llantas = llantas
        
    def mostrar_informacion(self):
        super().mostrar_informacion()    
        print(f"Llantas: {self.llantas}")
        
    def avanzar(self):
        print("La moto avanza...")
        
    def detener(self):
        print("La moto se detiene...")
        
        
class Caponera(Vehiculo):
    def __init__(self, marca, modelo, anio, pasajeros):
        super().__init__(marca, modelo, anio)
        self.pasajeros = pasajeros
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"La capacidad es de: {self.pasajeros}")
        
    def avanzar(self):
        print("La caponera avanza...")
        
    def detener(self):
        print("La caponera se detiene...")

caponera = Caponera("Yamaha", "X15", "2026", 4)
caponera.mostrar_informacion()
caponera.avanzar()
caponera.detener()

print("----------------------------------------------")

carro = Carro("Toyota", "Yaris", "2024", "Rosado")
carro.mostrar_informacion()
carro.avanzar()
carro.detener()
        