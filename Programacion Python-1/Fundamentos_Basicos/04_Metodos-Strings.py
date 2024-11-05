
Mascota = "  Sunny tierna  "

# Convierte los str de miniscula a mayuscula
print(Mascota.upper())

# Convierte los str de mayusculas a minusculas
print(Mascota.lower())

# Convierte a la primera letra de la primera palabra en mayuscula
print(Mascota.capitalize())

# Convierte la primera letra de cada palabra en mayusculas
print(Mascota.title())

# Elimina espacios tanto a la derecha como a la izquierda
print(Mascota.strip())

# Elimina espacios solo a la derecha
print(Mascota.rstrip())

# Elimina espacios soo a la izquierda
print(Mascota.lstrip())

# Busca algun caracter del str
print(Mascota.find("tier"))

# Reemplaza el caracter de cierta parte especifica del str que quieres por otro / estrucutura -> mascota.replace([Dato del str], [Nuevo dato] )
print(Mascota.replace("tierna", "Bella"))

# Pregunta si cierto caracter esta o no en el str -> Arroja dato boolean
print("ny" in Mascota)
print("bella" in Mascota)
print("F" not in Mascota)

# Forma de convinar metodos
print(Mascota.strip().title())
