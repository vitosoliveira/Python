def cpf_pra_num (string):
    numero=""
    for x in string:
        if x in '0123456789':
            numero = numero + x
    return int(numero)
