class Moto:
    def avanzar(self):
        print("Avanzando...")
    
    def detener(self):
        print("Deteniendose...")
        
class Barco:
    def flotar(self):
        print("Flotando...")
        
    def encender(self):
        print("Encendiendo...")
        
class MotoAcuatica(Moto, Barco):
    pass 

moto_acuatica = MotoAcuatica()
moto_acuatica.encender()
moto_acuatica.flotar()
moto_acuatica.avanzar()
moto_acuatica.detener()

    