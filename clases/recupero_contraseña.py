# clases/recupero_contraseña.py
from datetime import datetime, timedelta
import uuid

class RecuperoContraseña:
    def __init__(self, usuario_id):
        self.__usuario_id = usuario_id
        self.__token = None
        self.__fecha_solicitud = None
        self.__fecha_expiracion = None
        self.__usado = False

    def generar_token(self):
        self.__token = str(uuid.uuid4())
        self.__fecha_solicitud = datetime.now()
        self.__fecha_expiracion = self.__fecha_solicitud + timedelta(hours=1)
        self.__usado = False

    def validar_token(self, token_ingresado):
        if self.__usado:
            return False
        if self.__token != token_ingresado:
            return False
        if datetime.now() > self.__fecha_expiracion:
            return False
        return True

    def marcar_usado(self):
        self.__usado = True

    def get_token(self):
        return self.__token

    def get_fecha_solicitud(self):
        return self.__fecha_solicitud

    def get_fecha_expiracion(self):
        return self.__fecha_expiracion

    def fue_usado(self):
        return self.__usado
