class Empleado:
    def __init__(self, salario):
        self.salario = salario
        
    def calcular_salario(self):
        return self.salario
        
class Vendedor(Empleado):
    def __init__(self, salario, comision):
        super().__init__(salario)
        self.comision = comision
        
    def calcular_salario(self):
        return self.comision + self.salario
    
class Contrato(Empleado):
    def __init__(self, horas, tarifa):
        self.horas = horas
        self.tarifa = tarifa
    def calcular_salario(self):
         return self.horas * self.tarifa
     
     
Empleados = [
    Empleado(1000),
    Vendedor(500, 500),
    Contrato(5, 200)]

for empleado in Empleados:
    print(f"El empleado tiene un salario de: ${empleado.calcular_salario()}")
     
     
        
         
         
         
        