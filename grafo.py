from funções import *

def grafo(direcionado):
    
    while True:
        nVertices = verificaInteiro("Digite o número de vértices: ")
        if nVertices == 0:
            print("O grafo não possui vértices!")
            return
        elif nVertices == 1:
            print("\nO grafo possui um único vértice, logo, ele não possui arestas (Grafo trivial).")
            matrizAdj = inicializaMatriz(nVertices)
            print("\nMatriz do grafo trivial: ")
            imprimeMatriz(matrizAdj)
            print()
            return
        elif nVertices and nVertices < MAX_VÉRTICES and nVertices > 0:
            break
        else:
            print(f"O número de vértices deve estar entre 0 e {MAX_VÉRTICES}\n")

    matrizAdj = inicializaMatriz(nVertices)

    while True:
        print("\nOPERAÇÕES:\nAdicionar aresta [1]\nExcluir aresta [2]\nImprimir matriz [3]\nSair [0]")
        escolha = int(input("\nEscolha uma opção:"))

        escolha = int(escolha)

        if escolha > 3 or escolha < 0:
            print("\nVocê digitou uma opção inválida!\n")
    
        elif escolha == 1:
            if direcionado:
                x = obterVértice("Digite o vértice de saída: ", nVertices)
                y = obterVértice("Digite o vértice de entrada: ", nVertices)
                if not verificaConexão(matrizAdj, x, y):
                    adicionaAresta(matrizAdj, x, y, direcionado)
                else:
                    print(f"A conexão entre os vértices {x} e {y} já existe!")
            else:
                x = obterVértice("Digite o primeiro vértice: ", nVertices)
                y = obterVértice("Digite o segundo vértice: ", nVertices)
                if not verificaConexão(matrizAdj, x, y):
                    adicionaAresta(matrizAdj, x, y, direcionado)
                else:
                    print(f"A conexão entre os vértices {x} e {y} já existe!")

        elif escolha == 2:
            if direcionado:
                x = obterVértice("Digite o vértice de saída: ", nVertices)
                y = obterVértice("Digite o vértice de entrada: ", nVertices)
                if not verificaConexão(matrizAdj, x, y):
                    excluiAresta(matrizAdj, x, y, direcionado)
                else:
                    print(f"A conexão entre os vértices {x} e {y} já existe!")
            else:
                x = obterVértice("Digite o primeiro vértice: ", nVertices)
                y = obterVértice("Digite o segundo vértice: ", nVertices)
                if not verificaConexão(matrizAdj, x, y):
                    excluiAresta(matrizAdj, x, y, direcionado)
                else:
                    print(f"A conexão entre os vértices {x} e {y} já existe!")

        elif escolha == 3:
            imprimeMatriz(matrizAdj)

        elif escolha == 0:
            print("Encerrando...")
            break
