from clases.usuario import Usuario

usuario1 = Usuario(1, "Ana", "lopez", "12345667", "ana@example.com", "1234")

print(usuario1.get_nombre())
print(usuario1.get_apellido())
if usuario1.verificar_contraseña("1234"):
    print("Login correcto")
else:
    print("Contraseña incorrecta")


from clases.instructor import Instructor
from clases.clase_actividad import ClaseActividad

# Crear un instructor
instructor1 = Instructor(1, "Laura", "Giménez")

#print(instructor1.get_nombre_completo())

# Crear una clase de actividad con 2 cupos
clase1 = ClaseActividad(
    id_clase=101,
    nombre="Yoga Avanzado",
    cupo=2,
    dia="Martes",
    hora_inicio="19:00",
    hora_fin="20:00",
    instructor=instructor1
)

# Mostrar info inicial
print("INFO INICIAL DE LA CLASE:")
print(clase1.mostrar_info())
print()
