class ClaseActividad:
    def __init__(self, id_clase, nombre, cupo, dia, hora_inicio, hora_fin, instructor):
        self.id_clase = id_clase
        self.nombre = nombre
        self.cupo = cupo
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.instructor = instructor  # objeto tipo Instructor
        self.cupos_disponibles = cupo

    def crear_clase(self):
        pass

    def editar_clase(self, nuevos_datos):
        pass

    def eliminar_clase(self):
        pass

    def buscar_clase(self, criterio):
        pass

    def reducir_cupo(self):
        if self.cupos_disponibles > 0:
            self.cupos_disponibles -= 1
            return True
        return False

    def mostrar_info(self):
        return {
            "id": self.id_clase,
            "nombre": self.nombre,
            "día": self.dia,
            "horario": f"{self.hora_inicio} - {self.hora_fin}",
            "instructor": self.instructor.get_nombre_completo(),
            "cupos_disponibles": self.cupos_disponibles
        }
