from datetime import datetime

class Usuario:
    def __init__(self, id_usuario, nombre, apellido, documento, email, contraseña, tipo_usuario=True):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__documento = documento
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_alta = datetime.now()
        self.__tipo_usuario = tipo_usuario  # True = administrador, False = cliente

    # ==== Getters ====
    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_documento(self):
        return self.__documento

    def get_email(self):
        return self.__email

    def get_fecha_alta(self):
        return self.__fecha_alta

    def get_tipo_usuario(self):
        return self.__tipo_usuario

    # ==== Setters ====
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_apellido(self, nuevo_apellido):
        self.__apellido = nuevo_apellido

    def set_documento(self, nuevo_documento):
        self.__documento = nuevo_documento

    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña

    def set_tipo_usuario(self, tipo):
        self.__tipo_usuario = tipo

    # ==== Autenticación ====
    def verificar_contraseña(self, contraseña_ingresada):
        return self.__contraseña == contraseña_ingresada

    # ==== Métodos funcionales ====
    def registrarse(self):
        print(f"Usuario {self.__nombre} registrado correctamente.")

    def editar_perfil(self, datos_actualizados: dict):
        for clave, valor in datos_actualizados.items():
            if hasattr(self, f"_Usuario__{clave}"):
                setattr(self, f"_Usuario__{clave}", valor)

    def eliminar_usuario(self):
        print(f"Usuario {self.__id_usuario} eliminado del sistema.")

    def buscar_clase(self, lista_clases, nombre_buscado):
        return [clase for clase in lista_clases if clase.get_nombre().lower() == nombre_buscado.lower()]

    def filtrar_clase(self, lista_clases, dia):
        return [clase for clase in lista_clases if clase.get_dia().lower() == dia.lower()]

    def inscribirse_clase(self, clase):
        if clase.reducir_cupo():
            print(f"{self.__nombre} se inscribió correctamente en {clase.get_nombre()}.")
        else:
            print("No hay cupos disponibles para esta clase.")

    def mostrar_info(self):
        return {
            "id": self.__id_usuario,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "documento": self.__documento,
            "email": self.__email,
            "tipo_usuario": "administrador" if self.__tipo_usuario else "cliente",
            "fecha_alta": self.__fecha_alta.strftime("%Y-%m-%d %H:%M:%S")
        }
