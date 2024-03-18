import os
def mostrar_o_nome_do_jogo():
    print("Jogo Da Forca\n")

def escolher_e_esconder_a_palavra():
    mostrar_o_nome_do_jogo()
# escolha_a_palavra()
    palavra_chave = input("Escreva a palavra para ser descoberta:")

    # esconder_a_palavra
    tamanho_palavra = len(palavra_chave)
    palavra_escondida = ""
    quantidade_de_simbolos =  tamanho_palavra* "_"
    return quantidade_de_simbolos , palavra_chave

def hub_jogo(quantidade_de_simbolos, palavra_chave):   
    os.system("cls")
    erros = 0
    palavra = quantidade_de_simbolos
    while palavra != palavra_chave and erros < 5:
        os.system("cls")
        mostrar_o_nome_do_jogo()
        print(f"Palavra: {palavra}")
        palpite_letra = input("Digite a letra que deseja palpitar: ")
        if len(palpite_letra) != 1:
            print("Digite apenas uma letra por vez.")
        else:
            if palpite_letra in palavra_chave:
                nova_palavra = ""
                for i in range(len(palavra_chave)):
                    if palavra_chave[i] == palpite_letra:
                        nova_palavra += palpite_letra
                    else:
                        nova_palavra += palavra[i]
                palavra = nova_palavra
            else:
                erros += 1
                print(f"erros = {erros} (max : 5)")

    if erros < 5:
        print(f"Parabéns! Você descobriu a palavra: {palavra_chave}")
    else:
        print(f"Você excedeu o número máximo de erros. A palavra era: {palavra_chave}")

def main():
    quantidade_de_simbolos , palavra_chave = escolher_e_esconder_a_palavra()
    hub_jogo(quantidade_de_simbolos , palavra_chave)


if __name__ == "__main__":
    main()