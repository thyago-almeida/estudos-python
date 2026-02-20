conta = float(input("Digite o valor da conta: "))
pessoas = int(input("Digite o total de pessoas: "))

if pessoas != 0:
    individual = conta / pessoas
    taxa = conta * 0.10
    total_com_taxa = conta + taxa
    por_pessoa = total_com_taxa / pessoas

    print(f"O valor da conta é: R$ {individual:.2f}")
    print(f"O valor total com a taxa é: R$ {total_com_taxa:.2f}")
    print(f"O valor da conta com a taxa é: R$ {por_pessoa:.2f}")

else:
    print("A quantidade de pessoas não pode ser zero")



