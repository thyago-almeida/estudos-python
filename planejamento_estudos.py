horas_estudo = float(input("Digite quantas horas de estudo por dia: "))
qtd_dias = int(input("Digite a quantidade de dias por semana: "))

if qtd_dias != 0:
    horas_semana = horas_estudo * qtd_dias
    horas_mes = horas_semana * 4
    horas_ano = horas_mes * 12

    print(f"A quantidade de horas por semana é: {horas_semana:.2f}")
    print(f"A quantidade de horas por mês é: {horas_mes:.2f}")
    print(f"A quantidade de horas por ano é: {horas_ano:.2f}")
else:
    print("A quanidade de dias não pode ser zero")