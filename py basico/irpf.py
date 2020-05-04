def calculo_ir_bruto(dicionario, chave):
    if chave in dicionario:
        bruto = dicionario[0]
        if bruto < 22847.76:
            dicionario[chave] += [0]
        elif bruto < 33919.80:
            dicionario[chave] += bruto*0.075
        elif bruto < 45012.60:
            dicionario[chave] += bruto*0.15
        elif bruto < 55976.16:
            dicionario[chave] += bruto*0.225
        elif bruto >= 55976.16:
            dicionario[chave] += bruto*0.275


def calcula_deducao(dicionario, chave):
    if chave in dicionario:
        bruto = dicionario[chave][0]
        if bruto < 22847.76:
            dicionario[chave][2] = 0
        elif bruto < 33919.80:
            dicionario[chave][2] -= 1713.58
        elif bruto < 45012.60:
            dicionario[chave][2] -= 4257.57
        elif bruto < 55976.16:
            dicionario[chave][2] -= 7633.51
        elif bruto >= 55976.16:
            dicionario[chave][2] = 10432.32


def calcula_irpf_final(dicionario, chave):
    if chave in dicionario:
        dicionario[chave][2] -= dicionario[chave][1]
