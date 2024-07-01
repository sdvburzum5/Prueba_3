import random
import csv
import os

def main():
    lista_bitacoras = []
    while True:
        print('Menú')
        print('0. Limpiar pantalla')
        print('1. Jugar')
        print('2. Registrar bitácora')
        print('3. Listar bitácoras')
        print('4. Imprimir bitácoras')
        print('5. Buscar bitácora')
        print('6. Salir')
        opcion = input('Ingrese una opción:')
        if opcion == '0':
            limpiar_pantalla()
        elif opcion == '1':
            intentos = []
            for i in range(1, 4):
                jugada = int(input(f'Ingresa intento nro. {i}: '))
                intentos.append(jugada)
            print(intentos)
        elif opcion == '2':
            dados = [random.randint(1, 6), random.randint(1, 6), 1]
            nombre = input('Ingrese nombre: ').strip()
            apellido = input('Ingrese apellido: ').strip()
            nombre_completo = f'{nombre} {apellido}'
            nivel = input('Ingrese nivel: ').strip()
            bitacora = registrar_bitacora(dados, nombre_completo, nivel, intentos)
            if bitacora != None:
                lista_bitacoras.append(bitacora)
                for bitacora in lista_bitacoras:
                    print(bitacora)
        elif opcion == '3':
            listar_bitacora(lista_bitacoras)
        elif opcion == '4':
            nombre = input('Ingrese el nombre del archivo: ')
            imprimir_bitacora(nombre, lista_bitacoras)
        elif opcion == '5':
            nombre = input('Ingrese el nombre de la bitácora a buscar: ')
            if existe_bitacora(nombre, lista_bitacoras):
                ...
        elif opcion == '6':
            break
        else:
            print('Error: Ingrese una opción válida (1-6)')


def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')


def registrar_bitacora(dados, nombre_completo, nivel, intentos):
    if nivel not in ['Principiante', 'Intermedio', 'Experto']:
        print('Error: Ingrese nivel correcto (Principiante, Intermedio o Expero)')
        return
    bitacora = {
        'lanzamientos': dados,
        'jugador': nombre_completo,
        'nivel': nivel,
        'intento1': intentos[0],
        'intento2': intentos[1],
        'intento3': intentos[2]
    }
    return bitacora


def listar_bitacora(lista_bitacoras):
    print(f'{'Lanzamiento simulado':<25} {'Jugador':<25} {'Nivel':<20} {'Dado 1':<10} {'Dado 2':<10} {'Dado 3':<10}')
    for bitacora in lista_bitacoras:
        print(f'{bitacora["lanzamientos"]}')


def imprimir_bitacora(nombre, lista_bitacoras):
    if len(lista_bitacoras) == 0:
        print('Error: No hay bitacoras para guardar')
        return
    elif not nombre.endswith('.csv'):
        print('Error: El archivo debe ser formato .csv')
    with open(nombre, 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=['lanzamientos', 'jugador', 'nivel', 'intento1', 'intento2', 'intento3'])
        escritor.writeheader()
        for linea in escritor:
            escritor.writerow()

def buscar_bitacora():
    ...

def existe_bitacora(nombre, lista_bitacoras):
    for bitacora in lista_bitacoras:
        if bitacora['nombre'] == nombre:
            return True
    print('Error: La bitácora no existe')

main()