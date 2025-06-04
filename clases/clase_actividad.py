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
        self.inscriptos = []  # lista de usuarios

    def mostrar_info(self):
        return (f"Clase: {self.nombre} | Día: {self.dia} | Hora: {self.hora_inicio}-{self.hora_fin} | "
                f"Instructor: {self.instructor.get_nombre_completo()} | Cupos disponibles: {self.cupos_disponibles}")

    def editar_clase(self, nuevos_datos):
        for clave, valor in nuevos_datos.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)
        return True

    def eliminar_clase(self):
        # Esto sería más útil a nivel sistema, no dentro de la clase
        pass

    def buscar_clase(self, criterio):
        # Debería implementarse en una clase que administre varias clases
        pass

    def reducir_cupo(self):
        if self.cupos_disponibles > 0:
            self.cupos_disponibles -= 1
            return True
        return False

    def reservar_cupo(self, usuario):
        if self.cupos_disponibles > 0:
            self.inscriptos.append(usuario)
            self.reducir_cupo()
            return True
        return False
