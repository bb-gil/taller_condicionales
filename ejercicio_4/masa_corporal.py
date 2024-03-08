# entrada
peso = float(input("cual es  su peso: "))
altura = float(input("cual es su altura: "))

# processing 
IMC = peso/ altura**2

if IMC < 16:
    print("criterio de ingreso en hospital")
elif IMC <= 17:
    print("infrapeso") 
elif IMC <= 18.5:
    print("bajo peso")
elif IMC <= 25:
    print("peso normal(saludable)")
elif IMC <= 30:
    print("sobrepeso(obesidad de grado 1)")
elif IMC <= 35:
    print("sobrepeso cronico(obesidad de grado 2)")
elif IMC <= 40:
    print("obesidad premorbida(obesidad de grado 3)")
elif IMC > 40:
    print("obesidad morbida(obesidad de grado 4)")
print("su IMC es: ", IMC) 
          