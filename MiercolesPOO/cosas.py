class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        self.__nombre = nom
        self.__edad = self.set_edad(ed)
        self.__carrera = carr

    def set_nombre(self,nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_edad(self,ed):
        if ed >= 8 and ed <120:
            self.__edad = ed
        else:
            print("Esa edad no es correcta")

    def get_edad(self):
        return self.__edad

    def set_carrera(self,carr):
        self.__carrera = carr

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "---------------\n"
        cadena += "nombre: " +self.__nombre
        cadena += "\n" + str(self.__edad)
        cadena += "\n" +self.__carrera
        cadena += "\n---------------"
        return cadena

    def estudiar(self,horas=1):
        print(f"El alumno {self.__nombre} está estudiando por {horas} horas")

class Perro:
    reino = "Canino"
    def __init__(self,raza,edad,estatura):
        self.__raza = raza
        self.__edad = self.edad = edad
        self.__estatura = estatura

    #Método de acceso get
    @property
    def raza(self):
        return self.__raza

    #Método de acceso set
    @raza.setter
    def raza(self,raza):
        self.__raza = raza

    # Método de acceso get
    @property
    def edad(self):
        return self.__edad

    # Método de acceso set
    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            print('Esa no es una edad valida')

    # Método de acceso get
    @property
    def estatura(self):
        return self.__estatura

    # Método de acceso set
    @estatura.setter
    def estatura(self, estatura):
        if estatura > 0.1 and estatura < 1.1:
            self.__raza = estatura
        else:
            print("La estatura no es aceptada")
            self.__estatura = 0.1

    def __str__(self):
        return f"""
        ---------------------------
        | Raza: {self.__raza}
        | Edad: {self.edad}
        | Estatura: {self.__estatura}
        ---------------------------
        """

    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    @staticmethod
    def dormir(veces = 5):
        for n in range(veces):
            print(f"Dando vuelta {n + 1}")
        print("Zzzzzz")

    @classmethod
    def perro_grande(cls,est):
        if est > 0.79:
            return cls("",0,est)