from collections import deque

fila = deque()

fila.append('joão')
fila.append('alice')
fila.append('pedro')
print('fila atual',fila)

primeiro = fila.popleft()
print(f'primeiro removido: [primeiro]')
print(f'fila apos remocao', fila)

if not fila:
    print('a fila esta vazia')
else:
    print('a fila não esta vazia')
