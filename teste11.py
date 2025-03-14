while True:
    numero_1 = input('digite um número :')
    numero_2 = input('digite outro número :')
    operador = input('digite o operador (+-/*) :')

    numeros_validos = None


    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('um ou ambos os numeros digitados são invalidos')
        continue

    operadores_permitidos = '+-/*'
    if operador not in  operadores_permitidos:
        print('operador invalido')
        continue
    if len(operador) > 1:
        print('digite apenas um operador.')
        continue



    sair = input('quer sair? [s]im ').lower().startswith('s')
    print(sair)
    if sair is True:
        break
