#Função recursiva para encontra nº número da sequência de Fibonnaci
def fib_recursive(n):
    #Posição inválida
    if (n < 0):
        return False

    #Primeiras 2 posições são definidas
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    #Chamada recursiva
    return fib_recursive(n - 1) + fib_recursive(n - 2)

#Função iterativa/linear para encontra nº número da sequência de Fibonnaci
def fib_iterative(n):
    # Posição inválida
    if (n < 0):
        return False

    #Posição 0 não é coberta no for
    if (n == 0):
        return 0

    #Declaração dos valores na posições 0 e 1
    a = 0
    b = 1
    resposta = 1

    #Iterações
    for i in range(n - 1):
        b = resposta
        resposta = a + b
        a = b

    return resposta

if __name__ == "__main__":
    n = int(input("Valor de N: "))

    print("Função recursiva: ", fib_recursive(n))
    print("Função iterativa: ", fib_iterative(n))