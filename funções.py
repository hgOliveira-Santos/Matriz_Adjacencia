import numpy as np

MAX_VÉRTICES = 10

def inicializaMatriz(n):
    matriz = np.zeros((n, n), dtype="int")
    return matriz

def adicionaAresta(matriz, x, y, direcionado):    
    matriz[x][y] = 1
    if not direcionado:
        matriz[y][x] = 1
    
def excluiAresta(matriz, x, y, direcionado):
    if verificaConexão(matriz, x, y):
        matriz[x][y] = 0
        if not direcionado:
            matriz[y][x] = 0
    else:
        print(f"Não existe conexão entre os vértices {x} e {y}!")

def imprimeMatriz(matriz):
    for line in matriz:
        print(line)

def obterVértice(mensagem, numeroVertices):
    while True:
        vertice = verificaInteiro(mensagem)
        if vertice and verificaIntervalo(vertice, numeroVertices):
            return vertice
        print(f"\nVocê deve digitar um valor entre 0 e {numeroVertices-1}!\n")

def verificaIntervalo(n, limite):
    if n > limite:
        return False
    elif n < 0:
        return False
    else:
        return True

def verificaConexão(matriz, x, y):
    if matriz[x][y] != 0:
        return True
    return False

def verificaInteiro(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except ValueError:
            print("\nVocê deve digitar um número inteiro!\n")
            continue
        return n 
    
def verificaGrafoTrivial(numeroVértices):
    if numeroVértices == 1:
        return True