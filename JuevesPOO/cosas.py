class Autor:
    def __init__(self,nombre,pseudo):
        self.__nombre = nombre
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"""
                Nombre: {self.__nombre}"
                Pseudonimo: {self.__pseudonimo}
            """

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")


class Libro:
    def __init__(self,titulo,autor,anio,editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__editorial = editorial

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def titulo(self, anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    def __str__(self):
        return f"""
            ----------------------------
            Titulo: {self.__titulo}
            Autor: {self.__autor}
            Año: {self.__anio}
            Editorial: {self.__editorial}
            ----------------------------
            """

    @classmethod
    def libro_planeta(cls,titulo,autor,anio):
        return cls(titulo,autor,anio,"Planeta")

    def leer(self,minutos):
        print(f"Leyendo por {minutos}")

class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

class Alumno(Persona):
    def __init__(self,nombre,edad,num_cuenta,carrera,promedio):
        super().__init__(nombre,edad)
        self.__num_cuenta = num_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

    @property
    def num_cuenta(self):
        return self.__num_cuenta

    @num_cuenta.setter
    def num_cuenta(self, num_cuenta):
        self.__num_cuenta = num_cuenta

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio