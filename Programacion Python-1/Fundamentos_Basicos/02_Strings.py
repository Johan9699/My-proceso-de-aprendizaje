# Tipos de str(Comillas: dobles, simples,  -> solo se pueden usar en una sola linea
# triple dobles y triple simples)          -> estas son posibles usar en multiples lineas

Nombre_del_lenguaje_usado = "Python God"
Descripcion_del_lenguaje = """
Python,
lenguaje de alto nivel y sintaxis simple, 
perfecto para principiantes y mi favorito hasta ahora.
"""

# -> Determina la cantidad de caracteres Totales. (Los espacios tambien cuentan como caracteres)

len(Nombre_del_lenguaje_usado)
len(Descripcion_del_lenguaje)

# Si se desea acceder algún índice en especifico se usa la notación [] - Generalmente se enumera los caracteres desde el 0

print(Nombre_del_lenguaje_usado[0])
print(Nombre_del_lenguaje_usado[5])

# -> En este tipo de uso (donde se accede en un rango determinado por ti mismo) se enumera normalmente del 1 hasta la cantidad de caracteres

print(Nombre_del_lenguaje_usado[:2])
print(Nombre_del_lenguaje_usado[0:3])
print(Nombre_del_lenguaje_usado[7:])
