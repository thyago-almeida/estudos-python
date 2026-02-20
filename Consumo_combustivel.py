distancia = float(input("Qual a distância que será percorrida: "))
consumo = float(input("Quanto o carro consome de combustível: "))

if consumo != 0:
    litros = distancia / consumo
    print(f"Litros necessários: {litros:.2f}")
else:
    print("O consumo não pode ser zero.")                  