# Programa saber la ubicacion de x & y en el plano carteciano

# input
print("------------------------------------------------------")

x = int(input("digite la posicion de x en el plano: "))
y = int(input("digite la posicion de y en el plano: "))

# procesing
if x == 0:
    if y == 0:
        print(("la coordenada" ,(x , y), "esta en el origen"))
    else:
        print(("la coordenada" ,(x , y), "esta en el eje y"))
elif y == 0:
    print("la coordenada" ,(x , y),"esta en el eje X")
elif x > 0:
    if y > 0:
        print("la coordenada" ,(x , y),"esta en el cuadrante 1")
    else:
        print("la coordenada" ,(x , y),"estas en el cuadrante 4")
elif  y < 0:
    print("la coordenada" ,(x , y),"estas en el cuadrante 3")
else:
    print("la coordenada" ,(x , y),"estas en el cuadrante 2")                                      