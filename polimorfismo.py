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
        return self.salario + self.comision

class EmpleadoContrato(Empleado):
    def __init__(self, horas_trabajadas, tarifa):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa = tarifa
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa

Empleados = [
    Empleado(600),
    Vendedor(200, 250),
    EmpleadoContrato(48, 15)
]

for empleado in Empleados:
    print(f"El empleado(tipo = {type(empleado).__name__}) tiene un salario de: ${empleado.calcular_salario()}")