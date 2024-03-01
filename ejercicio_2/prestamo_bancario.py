# Programa para saber si se le permite acceder a un prestamo bancaria

# ENTRADA
Salario = int(input("cuanto es su salario : "))
Deuda = input("usted tiene otra deuda que no ha pagado (si o no) : ")

# Proceso y salida 
if Salario >= 945200:
    if Deuda == "no":
        print("su prestamo ha sido aprobado")
    else:
        print("su prestamo ha sido denegado")
elif Salario < 945200:
    print("su prestamo ha sido denegado")
                