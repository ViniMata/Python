def conta_soma(num1,num2):
    soma = num1 + num2
    print(f"A soma deu {soma}\n")
def conta_subtração(num1,num2):
    subtração = num1 - num2
    print(f"A subtração deu {subtração}\n")
def conta_multiplicação(num1,num2):
    multiplicação = num1 * num2
    print(f"A multiplicação deu {multiplicação}\n")
def conta_divisão(num1,num2):
    divisão = num1 / num2
    print(f"A divisão deu {divisão :.2f22}\n")
 
num1 = float(input("Numero 1: \n"))
num2 = float(input("Numero 2: \n"))

escolha = input("+, -, : ou x: ")
if escolha == "+":
    conta_soma(num1,num2)
elif escolha == "-":
    conta_subtração(num1,num2)
elif escolha == "x" or escolha== "X":
    conta_multiplicação(num1,num2)
elif escolha == ":":
    conta_divisão(num1,num2)
else:
    print("Você não escolheu nenhuma operação valida.")
