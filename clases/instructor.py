class Instructor:
    def __init__(self, instructor_id, nombre, apellido):
        self.instructor_id = instructor_id
        self.nombre = nombre
        self.apellido = apellido
        self.clases_asignadas = []

    def eliminar_clase(self, clase):
        if clase in self.clases_asignadas:
            self.clases_asignadas.remove(clase)

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def registrar_clase(self, clase):
        self.clases_asignadas.append(clase)

    def editar_clase(self, clase):
        # Esto depende de qué quieras editar, lo dejamos así por ahora
        pass
