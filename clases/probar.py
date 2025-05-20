from instructor import Instructor
from clase_actividad import ClaseActividad

# Crear un instructor
instructor1 = Instructor(1, "Laura", "Giménez")

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

# Intentar reservar 3 veces
for intento in range(1, 4):
    exito = clase1.reducir_cupo()
    if exito:
        print(f"Reserva #{intento} realizada con éxito ✅")
    else:
        print(f"Reserva #{intento} falló ❌ (No hay más cupos)")
    print(f"Cupos disponibles ahora: {clase1.cupos_disponibles}")

# Mostrar info final
print("\nINFO FINAL DE LA CLASE:")
print(clase1.mostrar_info())
