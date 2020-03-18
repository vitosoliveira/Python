def cpf_para_caracter(inteiro):
    cpf = ""
    inteiro = str(inteiro)
    if len(inteiro) == 11:
        for char in inteiro:
            if len(cpf)==3 or len(cpf)==7:
                cpf = cpf+"."+char
            elif len(cpf) == 11:
                cpf = cpf+"-"+char
            else:
                cpf = cpf+char
        return cpf
    else:
        return "String inválida"
