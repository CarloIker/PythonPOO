from cosas import Alumno, Perro

def main():
    al1 = Alumno('Carlo',20,'ICO')
    print(vars(al1))
    al1.__nombre = 'Iker'
    print(vars(al1))
    al1.set_nombre('CI')
    print(vars(al1))
    print(al1)
    al1.set_edad(150)
    al1.estudiar(4)
    print("------PERRO------")
    perro1 = Perro('Husky',5,0.90)
    print(vars(perro1))
    perro1.raza = "De la calle"
    print(vars(perro1))
    print(perro1.raza)
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

main()