from datetime import datetime

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, documento, email, contraseña):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento = documento
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_alta = datetime.now()
    
    # Getters
    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre
    
    def get_nombre(self):
        return self.__apellido
    
    def get_nombre(self):
        return self.__documento

    def get_email(self):
        return self.__email

    def get_fecha_alta(self):
        return self.__fecha_alta

    # Setters
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

        def set_nombre(self, nuevo_apellido):
        self.__nombre = nuevo_apellido

        def set_nombre(self, nuevo_documento):
        self.__nombre = nuevo_documento

    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    # Autenticación simple (ejemplo)
    def verificar_contraseña(self, contraseña_ingresada):
        return self.__contraseña == contraseña_ingresada

    def mostrar_info(self):
        return {
            "id": self.__id_usuario,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "documento": self.__documento,
            "email": self.__email,
            "fecha_alta": self.__fecha_alta.strftime("%Y-%m-%d %H:%M:%S")
        }
