numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicacao: ", multiplicacao)
if numero2 != 0:
    divisao = numero1 / numero2
else:
    print("Não é possível divisão por 0")