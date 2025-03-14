palavra_s = 'sabonete'
letras_acertadas = ''

while True:
    letra_digitada = input('digite uma letra: ')

    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue

    if letra_digitada in palavra_s:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_s:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print('*')



