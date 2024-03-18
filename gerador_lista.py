import os
list = []
titulo_lista = input("Qual o nome da sua lista? ")
while True:
    nome =  input("NOme:")
    if nome == "sair":
        break
    else:
        list.append(nome)
os.system("cls")
print(f"{titulo_lista}:\n")
for x in list:
    new = x.capitalize()
    print(f" -{new}")