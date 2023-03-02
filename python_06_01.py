# Escribe un script que dado la edad de una persona y su altura pueda determinar si la
# misma puede o no subirse en la montaña rusa “Push-Pull”, dado que se debe ser mayor a
# 14 años y tener una altura no menor de 1,62. El script debe ser capaz de informar si 
# puede o no subirse y en el caso de que no, porque razon (Si por edad, por tamaño u ambas)


EDAD_LIMITE = 14
ALTURA_LIMITE = 1.62

edad = input("¿Qué edad tienes? ")
edad = int(edad)
altura = input("¿Cuánto mides? ")
altura = float(altura)

edad_permitida = edad > EDAD_LIMITE
altura_permitida = altura > ALTURA_LIMITE

if edad_permitida and altura_permitida:
    print("¡Puedes subirte a la montaña rusa Push-Pull!")
else:
    if edad_permitida == False and altura_permitida == True:
        print("No tienes la edad suficiente para subirte a la montaña rusa Push-Pull")
    elif altura_permitida == False and edad_permitida == True:
        print("No tienes la altura suficiente para subirte a la montaña rusa Push-Pull")
    else:
        print(f"No puedes subirte a la montaña rusa Push-Pull porque tu edad debe ser mayor que {EDAD_LIMITE}, y tu altura no debe ser menor que {ALTURA_LIMITE}.")

    
