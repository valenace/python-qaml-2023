# Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:
# Cuántos años tiene.
# Si en lo que va del año ya cumplio o no.
# Determinar a qué generación pertenece:
# La generación silenciosa. Nacidos entre 1920 y 1939.
# Los baby boomers. Nacidos entre 1940 y 1959.
# Generación X. Nacidos entre 1960 y 1979.
# Generación Y o millennials. Nacidos entre 1980 y 1989.
# Generación Z. Nacidos entre 1990 en adelante.

AÑO_ACTUAL = 2023
MES_ACTUAL = 3
DIA_ACTUAL = 2

año = input("Año: ")
año = int(año)
mes = input("Mes: ")
mes = int(mes)
dia = input("Dia: ")
dia = int(dia)

print(80*"-")

edad = AÑO_ACTUAL - año
print(f"Tu edad es: {edad}")

meses_antes = (mes < MES_ACTUAL)
meses_despues = (mes > MES_ACTUAL)
mes_igual = (mes == MES_ACTUAL)

dias_antes = (dia < DIA_ACTUAL)
dias_despues = (dia > DIA_ACTUAL)
dia_igual = (dia == DIA_ACTUAL)

print(80*"-")
if (dia_igual) and (mes_igual):
    print("Feliz cumpleaños!")
elif (dias_antes) and (mes_igual):
    print("Ya cumpliste años")
elif (dia_igual) and (meses_antes):
    print("Ya cumpliste años")
elif (dias_despues) and (meses_antes):
    print("Ya cumpliste años")
elif (dias_antes) and (meses_antes):
    print("Ya cumpliste años")    
else:
    print("No has cumplido años")



print(80*"-")
if año <= 1939:
    print("Generación silenciosa")
elif año <= 1959:
    print("Baby boomers")
elif año <= 1979:
    print ("Generación X")
elif año <= 1989:
    print("Generación Y")
else:
    print("Generación Z")