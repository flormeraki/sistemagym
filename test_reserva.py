from clases.usuario import Usuario
from clases.instructor import Instructor
from clases.clase_actividad import ClaseActividad

# Crear usuario
usuario1 = Usuario(1, "Ana", "Lopez", "12345667", "ana@example.com", "1234")
usuario2 = Usuario(2, "Luis", "Martínez", "23456789", "luis@example.com", "pass456")
usuario3 = Usuario(3, "Luis", "Martínez", "23456789", "luis@example.com", "pass456")

# Crear instructor
instructor1 = Instructor(1, "Laura", "Giménez")

# Crear clase con cupo
clase_yoga = ClaseActividad(
    id_clase=1,
    nombre="Yoga",
    cupo=2,
    dia="Martes",
    hora_inicio="19:00",
    hora_fin="20:00",
    instructor=instructor1
)

# Reservar clase
reserva_exitosa = clase_yoga.reservar_cupo(usuario1)

# Ver resultado
if reserva_exitosa:
    print("✅ Reserva realizada con éxito.")
else:
    print("❌ No hay cupos disponibles.")

# Reservas
reserva1 = clase_yoga.reservar_cupo(usuario1)
print("✅ Reserva 1:", "OK" if reserva1 else "❌ Sin cupo")

reserva2 = clase_yoga.reservar_cupo(usuario2)
print("✅ Reserva 2:", "OK" if reserva2 else "❌ Sin cupo")

reserva3 = clase_yoga.reservar_cupo(usuario3)
print("✅ Reserva 3:", "OK" if reserva3 else "❌ Sin cupo")  # Esta debería fallar