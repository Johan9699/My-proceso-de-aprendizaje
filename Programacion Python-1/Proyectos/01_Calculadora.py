# Los imputs
Num1 = input("ESCRIBE UN NÚMERO ")
Operador = input("Escribe Operador(+, -, *, /, **) ")
Num2 = input("ESCRIBE EL SEGUNDO NÚMERO ")

# Convertir los imputs en un tipo de variable especifico
Num1 = int(Num1)
Num2 = int(Num2)
Operador = str(Operador)

# Resultado -> En str
Resultado = f"{Num1} {Operador} {Num2}"

# Condiciones -> creamos condiciones para imprimir el operador que corresponde
if Resultado == f"{Num1} + {Num2}":
    print("ES IGUAL A: ", Num1 + Num2)

if Resultado == f"{Num1} - {Num2}":
    print("ES IGUAL A: ", Num1 - Num2)

if Resultado == f"{Num1} * {Num2}":
    print("ES IGUAL A: ", Num1 * Num2)

if Resultado == f"{Num1} / {Num2}" and Num2 != 0:
    print("ES IGUAL A: ", Num1 / Num2)
if f"{Num1} / {Num2}" and Num2 == 0:
    print("Resultado indefinido")

if Resultado == f"{Num1} ** {Num2}":
    print("ES IGUAL A: ", Num1 ** Num2)
