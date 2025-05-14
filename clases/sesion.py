# clases/sesion.py
from datetime import datetime

class Sesion:
    def __init__(self, usuario_id):
        self.__usuario_id = usuario_id
        self.__activo = False
        self.__hora_inicio = None
        self.__hora_fin = None

    def iniciar_sesion(self):
        self.__activo = True
        self.__hora_inicio = datetime.now()

    def cerrar_sesion(self):
        self.__activo = False
        self.__hora_fin = datetime.now()

    def esta_activa(self):
        return self.__activo

    def get_usuario_id(self):
        return self.__usuario_id

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_fin(self):
        return self.__hora_fin
