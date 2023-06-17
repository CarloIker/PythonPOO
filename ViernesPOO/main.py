from cosas import *

def main():
    per1=Persona("José", 19)
    print(per1)
    print(Persona.descripcion)
    print("----herencia alumno----")
    al1=Alumno("José",19,"12345678", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2=Alumno.constructor_defecto()
    print(al2)
    al2.nombre="Angel"
    print(al2)
    al2.dormir()

    print("---herencia profesor----")
    prof1=Profesor("Jesús",30+16,123456789,"Ingeniería de software")
    print(prof1)
    prof1.dormir()

    print("---herencia ayudante---")
    ayudante=AyudanteProfesor("Adrían",20,"98765432", "ICO",784656,"Ing de software" ,4)
    ayudante.dormir()
    print(ayudante)
main()