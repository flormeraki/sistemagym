
from clases.usuario import Usuario
from clases.instructor import Instructor
from clases.clase_actividad import ClaseActividad



usuario1 = Usuario(1, "Ana", "lopez", "12345667", "ana@example.com", "1234")

print(usuario1.get_nombre())
print(usuario1.get_apellido())
if usuario1.verificar_contraseña("1234"):
    print("Login correcto")
else:
    print("Contraseña incorrecta")


# from clases.instructor import Instructor
# from clases.clase_actividad import ClaseActividad

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

# from clase_actividad import ClaseActividad
#  instructor import Instructor

# Crear un instructor
instructor_juan = Instructor(instructor_id=1, nombre="Juan", apellido="Pérez")

# Crear clases
spinning = ClaseActividad(
    id_clase=1,
    nombre="Spinning",
    cupo=10,
    dia="Lunes",
    hora_inicio="18:00",
    hora_fin="19:00",
    instructor=instructor_juan
)

yoga = ClaseActividad(
    id_clase=2,
    nombre="Yoga",
    cupo=8,
    dia="Martes",
    hora_inicio="17:00",
    hora_fin="18:00",
    instructor=instructor_juan
)
from clases.clase_actividad import ClaseActividad
# Lista de clases
clases_disponibles = [spinning, yoga]

# Mostrar info de todas las clases
print("📅 Clases disponibles:")
for clase in clases_disponibles:
    print(clase.mostrar_info())

# Filtrar clases por día
def filtrar_por_dia(clases, dia):
    return [clase for clase in clases if clase.dia.lower() == dia.lower()]

# Ejemplo: filtrar clases del martes
print("\n🔍 Clases para el martes:")
clases_martes = filtrar_por_dia(clases_disponibles, "Martes")
for clase in clases_martes:
    print(clase.mostrar_info())

# Ejemplo: modificar clase
print("\n✏️ Modificando clase SPINNING...")
spinning.editar_clase({
    "nombre": "Spinning Intermedio",
    "dia": "Miércoles",
    "hora_inicio": "19:30",
    "hora_fin": "20:30"
})

print("✅ Clase modificada:")
print(spinning.mostrar_info())

# Ejemplo: eliminar clase por id

def eliminar_clase_por_id(clases, id_buscado):
    return [clase for clase in clases if clase.id_clase != id_buscado]

print("\n🗑️ Eliminando clase con ID 2 (Yoga)...")
clases_disponibles = eliminar_clase_por_id(clases_disponibles, 2)

print("📋 Clases restantes:")
for clase in clases_disponibles:
    print(clase.mostrar_info())


