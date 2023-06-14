from cosas import Alumno

def main():
    """
    al1 = Alumno()
    print(al1)
    al2 = Alumno()
    print(al1.facultad)
    print(al2.facultad)
    print("-----------")
    Alumno.facultad = "UNAM FES Aragon"
    print(al1.facultad)
    print(al2.facultad)
    print("-----------")
    print(vars(al1))
    print(vars(al2))
    al1.edad = 999
    print(vars(al1))
    print(vars(al2))
    """
    al1 = Alumno("Carlo",20,"ICO")
    al2 = Alumno("Angel",23,"ICO")
    al1.__edad = 333
    print(vars(al1))
    print(vars(al2))

main()
