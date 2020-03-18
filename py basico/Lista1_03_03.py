def calcular_media(dicionario, nome):
    media = 0
    if nome in dicionario:
        for nota in dicionario[nome]:
            media += nota
        return media/len(dicionario[nome])
    else:
        return 0