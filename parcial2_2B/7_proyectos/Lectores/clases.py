class Lectores:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.reserva = None
        self.entrega = None

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self, direccion):
        self.direccion = direccion

    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono

    # Métodos
    def setReservar(self, reserva):
        self.reserva = reserva
    
    def getReservar(self):
        return self.reserva
    
    def setEntrega(self, entrega):
        self.entrega = entrega

    def getEntrega(self):
        return self.entrega

    # Información
    def getInfo1(self):
        print(f"{self.getNombre()}, con dirección: {self.getDireccion()}, num_telefono: {self.getTelefono()}")

class Estudiante(Lectores):
    def __init__(self, nombre, direccion, telefono, carrera, matricula):
        super().__init__(nombre, direccion, telefono)
        self._carrera = carrera # Atributo privado
        self._matricula = matricula # Atributo privado
    #atributos
    def getCarrera(self):
        return self._carrera
    
    def setCarrera(self, carrera):
        self._carrera = carrera
    
    def getMatricula(self):
        return self._matricula

    #informacion
    def getInfo2(self):
        print(f"El alumno: {self.getNombre()} con dirección: {self.getDireccion()}, num_telefono: {self.getTelefono()}, estudia la carrera de {self.getCarrera()} y su matrícula es {self.getMatricula()}")


class Docentes(Lectores):
    def __init__(self, nombre, direccion, telefono, modalidad, num_empleado):
        super().__init__(nombre, direccion, telefono)
        self.__modalidad = modalidad
        self.__num_empleado = num_empleado
    #atributos
    def getModalidad(self):
        return self.__modalidad
    
    def getNumEmpleado(self):
        return self.__num_empleado
    #informaion
    def getInfo3(self):
        print(f"El Docente: {self.getNombre()} con dirección: {self.getDireccion()}, num_telefono: {self.getTelefono()}, está en la modalidad de {self.getModalidad()}, su número de empleado es {self.getNumEmpleado()}")

#fin de las clases

#termino: 28/06/2024
#hora de terminacion: 11:05 a.m.