def contagemregresiva(n):
    if n == 0:
        print('decolar!')
    else:
        print(n)
        contagemregresiva(n-1)
contagemregresiva(5)
    

