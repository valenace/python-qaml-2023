# Pide al usuario dos variables a = 12 y b = 34, crea funciones que permitan calcular la suma, resta, multiplicación y división, como también el valor del módulo de b entre a


# Suma
def suma_operacion(numero_a : int, numero_b : int):
    print(f"Operación suma: {numero_a} + {numero_b}")
    return numero_a + numero_b

# Resta
def resta_operacion(numero_a : int, numero_b : int):
    print(f"Operación resta: {numero_a} - {numero_b}")
    return numero_a - numero_b

# Multiplicacion
def multiplicacion_operacion(numero_a : int, numero_b : int):
    print(f"Operación multiplicacion: {numero_a} * {numero_b}")
    return numero_a * numero_b

# Division
def division_operacion(numero_a : int, numero_b : int):
    print(f"Operación divisón: {numero_a} // {numero_b}")
    return numero_a // numero_b

# Modulo
def modulo_operacion(numero_a : int, numero_b : int):
    print(f"Operación modulo: {numero_b} % {numero_a}")
    return numero_a % numero_b

primer_numero = input("Inserte número A: ")
segundo_numero = input("Inserte número B: ")
primer_numero = int(primer_numero)
segundo_numero = int(segundo_numero)
print (80 * "-")
print (f"Resultado de la suma: {suma_operacion(primer_numero, segundo_numero)}")
print (80 * "-")
print (f"Resultado de la resta: {resta_operacion(primer_numero, segundo_numero)}")
print (80 * "-")
print (f"Resultado de la multiplicacion: {multiplicacion_operacion(primer_numero, segundo_numero)}")
print (80 * "-")
print (f"Resultado de la division: {division_operacion(primer_numero, segundo_numero)}")
print (80 * "-")
print (f"Resultado del modulo: {modulo_operacion(primer_numero, segundo_numero)}")
print (80 * "=")


# Crea una función que permita convertir cualquier numero entero y a flotante
def entero_a_flotante(numero_entero : int):
    return float(numero_entero)
cualquier_numero = input("Inserte cualquier número: ")
cualquier_numero = int(cualquier_numero)
print (80 * "-")
print (f"Conversión de numero entero a flotante: {entero_a_flotante(cualquier_numero)}")
print (80 * "=")


# Extra: Define una función para convertir de grados Celsius a Fahrenheit, pide al usuario que ingrese la temperatura en Celsius e imprima la conversión.
def celsius_a_fahrenheit(grados_celsius:int):
    print (80 * "=")
    conversion_grados = (grados_celsius * 1.8) + 32
    return int(conversion_grados)

celsius_numero = input("Inserte la temperatura en Celsius: ")
celsius_numero = int(celsius_numero)
print (80 * "-")
print (f"Conversión de grados Celsius a Fahrenheit: {celsius_a_fahrenheit(celsius_numero)} °F")