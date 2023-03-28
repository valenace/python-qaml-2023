import random
from os import path
lista_partidas = []
lista_jugadores = []
lista_jugadores_activos = []
player = []
class Partida:

    def __init__(self,numero, jugador_a, jugador_b) -> None:
        self._numero = numero
        self._jugador_a = jugador_a
        self._jugador_b = jugador_b
        self._estado = 'ACTIVA'
        self._ganador = 'NINGUNO'

    def get_nombre(self):
        return self._numero
    
    def get_jugador_a(self):
        return self._jugador_a

    def get_jugador_b(self):
        return self._jugador_b
    
    def set_estado(self,estado):
        self._estado = estado
    
    def set_ganador(self,ganador):
        self._ganador = ganador  
          
    def get_ganador(self):
        return self._ganador
        
    def get_estado(self):
        return self._estado

class Jugador:

    def __init__(self,nombre, mail, raza,estado='ACTIVO'):
        self._nombre = nombre
        self._mail = mail
        self._raza = raza
        self._estado = estado
        self._puntos = 0
        self._partidas = 0

    def get_nombre(self):
        return self._nombre
    
    def get_mail(self):
        return self._mail

    def get_raza(self):
        return self._raza

    def set_estado(self,estado):
        self._estado = estado

    def get_estado(self):
        return  self._estado
    
    def set_puntos(self,puntos):
        self._puntos += puntos
    

    def contar_partida(self):
        self._partidas += 1

    def get_puntos(self):
        return self._puntos
    
    def get_partidas(self):
        return self._partidas
    
    # def __str__(self):
    #     return '{self._nombre} - {self._mail} - {self._raza} - {self._puntos} - {self._partidas}'.format(self._nombre,self._mail,self._raza,self._puntos,self._partidas)
    
_jugadores_file = 'jugadores_file.txt'
__partidas_file = 'partidas_file.txt'

def limpiar_registros():
    with open(_jugadores_file,'w') as file:
        pass
    with open(__partidas_file,'w') as file:
        pass
    
def exportar_jugadores(jugador:Jugador):
    with open(_jugadores_file,'a') as file:
        file.write('{},{},{},{} puntos,{} partidas\n'.format(jugador.get_nombre(),jugador.get_mail(),jugador.get_raza(), jugador.get_puntos(),jugador.get_partidas()))
    if (jugador.get_puntos() == 6):
        with open(_jugadores_file,'a') as file:
            file.write('GANADOR DEL TORNEO: {}\n'.format(jugador.get_nombre()))
   
def exportar_partidas(partida:Partida):
    with open(__partidas_file,'a') as file:
        file.write('Partida: {}, GANADOR: {} \n'.format(partida.get_nombre(), partida.get_ganador()))
 
def disponible():
    jugadores = len(lista_jugadores_activos)
    if (jugadores) < 4:
        return True
    else:
        return False
    
def create_random_partida():
    index_a = random.randint(0,len(lista_jugadores_activos)-1)
    jugador_a = lista_jugadores_activos[index_a]
    while jugador_a.get_estado() == 'JUGANDO':
        index_a = random.randint(0,len(lista_jugadores_activos)-1)
        jugador_a = lista_jugadores_activos[index_a]
    
    index_b = random.randint(0,len(lista_jugadores_activos)-1)
    jugador_b = lista_jugadores_activos[index_b]
    while index_b == index_a or jugador_b.get_estado() == 'JUGANDO':
        index_b = random.randint(0,len(lista_jugadores_activos)-1)
        jugador_b = lista_jugadores_activos[index_b]
    
    nombre_partida = f'{jugador_a.get_nombre()} VS {jugador_b.get_nombre()}'
    partida = Partida(nombre_partida,jugador_a,jugador_b)
    lista_partidas.append(partida)
    lista_jugadores_activos[index_a].set_estado('JUGANDO')
    lista_jugadores_activos[index_b].set_estado('JUGANDO')

def create_partidas():
    jugadores_activos = True
    while jugadores_activos:
        create_random_partida()
        index = 0
        jugador = lista_jugadores_activos[index]
        while jugador.get_estado() != 'ACTIVO' and index < len(lista_jugadores_activos) - 1:
            index += 1
            jugador = lista_jugadores_activos[index]
        if index == len(lista_jugadores_activos) - 1:
            jugadores_activos = False
 
def finalizar_partida_random():
    for partida in lista_partidas:
        index = random.randint(0,1)
        if partida.get_estado() == 'ACTIVA':
            if index == 0:
                jugador_a = partida.get_jugador_a()
                jugador_a.set_puntos(3)
                jugador_a.contar_partida()
                jugador_a.set_estado('ACTIVO')
                jugador_b = partida.get_jugador_b()
                jugador_b.set_puntos(1)
                jugador_b.contar_partida()
                jugador_b.set_estado('INACTIVO')
                index = 0
                jugador_perdedor = lista_jugadores_activos[index]
                while jugador_b.get_nombre() != jugador_perdedor.get_nombre() and index < len(lista_jugadores_activos) - 1:
                        index += 1
                        jugador_perdedor = lista_jugadores_activos[index]
                lista_jugadores_activos.pop(index)
                # ganador=jugador_a.get_nombre()
                print(f'GANADOR: {jugador_a.get_nombre()}')
                partida.set_ganador(jugador_a.get_nombre())
            else:
                jugador_a = partida.get_jugador_b()
                jugador_a.set_puntos(3)
                jugador_a.contar_partida()
                jugador_a.set_estado('ACTIVO')
                jugador_b = partida.get_jugador_a()
                jugador_b.set_puntos(1)
                jugador_b.contar_partida()
                jugador_b.set_estado('INACTIVO')
                index = 0
                jugador_perdedor = lista_jugadores_activos[index]
                while jugador_b.get_nombre() != jugador_perdedor.get_nombre() and index < len(lista_jugadores_activos) - 1:
                        index += 1
                        jugador_perdedor = lista_jugadores_activos[index]
                lista_jugadores_activos.pop(index)
                print(f'GANADOR: {jugador_a.get_nombre()}')
                partida.set_ganador(jugador_a.get_nombre())
            partida.set_estado('FINALIZADA')

def finalizar_partidas():
    jugadores_jugando = True
    while jugadores_jugando:
        finalizar_partida_random()
        index = 0
        jugador = lista_jugadores_activos[index]
        while jugador.get_estado() != 'JUGANDO' and index < len(lista_jugadores_activos) - 1 :
            index += 1
            jugador = lista_jugadores_activos[index]
        if index == len(lista_jugadores_activos) - 1:
            jugadores_jugando = False

limpiar_registros()

opcion = int(input('''Ingrese una opcion (1 para agregar jugador, 2 para iniciar campeonato, 0 para salir)\n'''))

TERRAN = 'Terran'
PROTOSS = 'Protoss'
ZERG = 'Zerg'    

while opcion != 0:
    if opcion == 1:
        if disponible():
            print('---- Agregar Jugador ----')
            nombre = input('Ingrese nombre del jugador\n')
            mail = input('Ingrese mail del jugador\n')
            raza_input = input('seleccione raza del jugador (t = Terran, z = Zerg, p = Protoss) \n')
            if raza_input == 't':
                raza_player = TERRAN
            elif raza_input == 'z':
                raza_player = ZERG
            elif raza_input == 'p':
                raza_player = PROTOSS
            else:
                print('opcion invalida')
            player = Jugador(nombre,mail,raza_player) 
            lista_jugadores.append(player)
            lista_jugadores_activos.append(player)
        else:
            print('------------------------------------')
            print('-    Cantidad de cupo cubierto    -')
            print('--=---------------------------------') 
            opcion = int(input('''Ingrese una opcion (1 para agregar jugador, 2 para iniciar campeonato, 0 para salir)\n'''))
    elif opcion == 2:
        if not disponible():            
            # Primera Ronda
            create_partidas()
            for partida in lista_partidas:
                print(partida.get_nombre())
            finalizar_partidas()            
            print('------------------------')
            for jugador in lista_jugadores_activos:
                print(jugador.get_nombre())

            # Segunda Ronda
            print('Segunda Ronda')
            create_partidas()
            finalizar_partidas()
            for partida in lista_partidas:
                if partida.get_estado() == 'FINALIZADA':
                    exportar_partidas(partida)                
            print('------------------------')
            for jugador in lista_jugadores:
                print(f'{jugador.get_nombre()} - {jugador.get_puntos()} - {jugador.get_puntos()}')
                exportar_jugadores(jugador) 
            
            print('------------------------')
            print('Torneo finalizado')
            break
        else:
            print('------------------------------------')
            print('- Cantidad de jugadores incompleto -')
            print('--=---------------------------------') 
            opcion = int(input('''Ingrese una opcion (1 para agregar jugador, 2 para iniciar campeonato, 0 para salir)\n'''))   
    
    else:
        print('opcion invalida')
        opcion = int(input('''Ingrese una opcion (1 para agregar jugador, 2 para iniciar campeonato, 0 para salir)\n'''))
