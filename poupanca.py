salario = float(input("Digite o seu salário: "))
percentual = int(input("Digite o percentual que consegue guardar: "))

decimal = percentual / 100
mes = salario * decimal
ano = mes * 12

print(f"No mês é poupado: R$ {mes:.2f}")
print(f"No ano é poupado: R$ {ano:.2f}")