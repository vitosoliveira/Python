import irpf
##Vitor Soares de Oliveira 1901878

dicionario = {12345678900: [35048.00, 140.65]}

irpf.calcula_ir_bruto(dicionario, 12345678900)
irpf.calcula_deducao(dicionario, 12345678900)
irpf.calcula_irpf_final(dicionario, 12345678900)

for pessoa in dicionario:
    cpf = ""
    if pessoa < 12:
        cpf = pessoa[:3] + "." + pessoa[3:6] + "."
        cpf += pessoa[6:9] + "-" + pessoa[9:]
    else:
        cpf = pessoa
    if dicionario[pessoa][2] > 0:
        print("CPF:", cpf, "- Deverá pagar R$", end="")
        print("%.2f" % dicionario[pessoa][2], "de IRPF.")
    elif dicionario[pessoa][2] < 0:
        print("CPF:", cpf, "- Receberá restituição de R$", end="")
        print("%.2f" % dicionario[pessoa][2])
    elif dicionario[pessoa][2] == 0:
        print("CPF:", cpf, "- Sem pendências com a Receita.")
