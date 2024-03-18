import os
list = []
os.system("cls")
titulo_lista = input("Qual o nome da sua lista? ")
while True:
    nome =  input("Item da lista:")
    input("Digite 'sair' na proxima linha para sair")
    if nome != 'sair':
        list.append(nome)
    elif nome == "sair":
        break
os.system("cls")
print(f"{titulo_lista}:\n")
for x in list:
    new = x.capitalize()
    print(f" -{new}")