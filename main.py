from clases.usuario import Usuario

usuario1 = Usuario(1, "Ana López", "ana@example.com", "1234")

print(usuario1.get_nombre())

if usuario1.verificar_contraseña("1234"):
    print("Login correcto")
else:
    print("Contraseña incorrecta")
