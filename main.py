from grafo import grafo

def main():
    
    while True:

        print("Tipos de grafos:")
        print("Direcionados - D")
        print("Não direcionados - N")

        tipo = input("\nEscolha uma opção: ")
    
        if tipo == "d":
            grafo(direcionado=True)
            break
        elif tipo == "n":
            grafo(direcionado=False)
            break
        else:
            print("Você digitou um caracter inválido! Tente novamente.\n")
        

if __name__ == "__main__":
    main()