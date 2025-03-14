def hanoi(n, torre1, torre2, torre3):
    if n == 1:  # Caso base: Se houver apenas 1 disco, basta movê-lo diretamente para a torre de destino.
        print(f"Mova o disco 1 da {torre1} para a {torre2}")
        return  # Retorna, pois não há mais discos para mover.
    
    # Passo 1: Move os n-1 discos da torre1 para a torre3, usando torre2 como auxiliar.
    hanoi(n - 1, torre1, torre3, torre2)
    
    # Passo 2: Move o disco restante (o maior) da torre1 para a torre2 (destino).
    print(f"Mova o disco {n} da {torre1} para a {torre2}")
    
    # Passo 3: Move os n-1 discos da torre3 para a torre2, usando torre1 como auxiliar.
    hanoi(n - 1, torre3, torre2, torre1)

# Definir o número de discos
n = 5

# Chamar a função hanoi com os parâmetros:
# - Número de discos
# - Torre de origem (Torre A)
# - Torre de destino (Torre C)
# - Torre auxiliar (Torre B)
hanoi(n, 'Torre A', 'Torre C', 'Torre B')


