import numpy as np
import random

def validar_numero(input_str):
    if not input_str:
        return "Error: El campo no puede estar vacío"
    try:
        numero = int(input_str)
        if (60 <= numero <= 120):
            return int(input_str)
        else:
            return "Error: El número debe estar entre 60 y 120"
    except ValueError:
        return "Error: Debes ingresar un número entero válido"

def validar_porcentaje(input_str):
    if not input_str:
        return "Error: El campo no puede estar vacío"
    try:
        numero = int(input_str)
        if (0 <= numero <= 100):
            return int(input_str)
        else:
            return "Error: El número debe estar entre 60 y 120"
    except ValueError:
        return "Error: Debes ingresar un número entero válido"


def generarconocidos(elec):
    matriz=np.zeros((elec,elec), dtype = int)
    n = matriz.shape[0]  #obtiene el tamaño de la matriz sin elec
    for x in range(n):
        conexiones_deseadas = random.randint(0, 5)  #genera un numero de conexiones deseadas entre 0 y 5
        while np.sum(matriz[x]) < conexiones_deseadas:  #asegura que las conexiones deseadas se cumplan
            intentos = list(range(n))
            random.shuffle(intentos)  #mezcla aleatoriamente
            for y in intentos:
                if x != y and matriz[x][y] == 0 and np.sum(matriz[y]) < 5:
                    matriz[x][y] = 1
                    matriz[y][x] = 1
                    break  
            if all(np.sum(matriz[y]) >= 5 or matriz[x][y] == 1 for y in range(n)):
                #all() asegura que todo sea verdadero
                break 
    return matriz
            
#Verificador de matriz asimetrica
def matrizasivef(matriz):
	if not np.array_equal(matriz, matriz.T):
		return "\nLa matriz es asimétrica."
	else:
		return "\nLa matriz es simétrica."

#calcular dias de contagio
def calcular_dias_contagio(matriz, eleccion_porcentaje_empresa):
    longitud = matriz.shape[0]
    paciente_zero = random.randint(0, longitud - 1)
    personas_contagiadas = set([paciente_zero])  #set para que no se repitan los contagiados
    personas_del_porcentaje = (longitud * eleccion_porcentaje_empresa) // 100
    dias = 0

    if personas_del_porcentaje > longitud:
        return "No se pueden contagiar todos los miembros del porcentaje indicado."
    while len(personas_contagiadas) < personas_del_porcentaje:
        nuevos_contagiados = set() #set es lo mejor
        for persona in personas_contagiadas:
            for i, contacto in enumerate(matriz[persona]):
                if contacto == 1 and i not in personas_contagiadas:
                    nuevos_contagiados.add(i)
        if not nuevos_contagiados:  
            break
        personas_contagiadas.update(nuevos_contagiados)
        dias += 1

    return dias if len(personas_contagiadas) >= personas_del_porcentaje else -1  # Retorna -1 si no se alcanza el objetivo
# lo que mas tardó
def guardarmatriz(save,matriz):
    if save == 'Guardar': np.savetxt("Matriz Booleana xdxd.txt",matriz,fmt="%d"); print("Matriz Guardada")