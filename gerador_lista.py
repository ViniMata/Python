list = []
while True:
    nome =  input("NOme:")
    if nome == "sair":
        break
    else:
        list.append(nome)
for x in list:
    new = x.capitalize()
    print(f"-{new}")