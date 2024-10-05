num1 = int(input("Digite o primeiro numero inteiro: "))

num2 = int(input("Degite o segundo numero inteiro: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(abs(num1 - num2))
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)  
else:
    print("Operação invalida") 