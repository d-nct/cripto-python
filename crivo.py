# Pseudocódigo
# ------------
    # 1. cria lista de tamanho n, com elementos True
    # 2. caso base para evitar divisão por 0 e porque divisão por 1 não é critério para verificação de primos
    # 3. percorremos a lista
    # 3.1. se L[i] == True
    # 3.2. seus múltiplos (a partir de i**2) viram False
    # 4. retorna o conjunto de primos

def crivo (n):
    """Retorna o conjunto de primos até  n, utilizando o método do Crivo de Erastótenes.
    Ressalta-se que n representa o intervalo semiaberto [0,n[
    
    Exemplo
    -------
    >>> crivo (10)
    {2, 3, 5, 7}
    >>> crivo (7)
    {2, 3, 5}
    """
    assert (isinstance(n, int)), "Para que a função funcione, n deve ser inteiro."
    
    primos = set({})
    #1.
    L = [True for _ in range (n)]
    #2.
    L[0], L[1] = False, False
    #3.
    for i in range (n):
        #3.1
        if L[i] == True:
            primos.add(i)
            for j in range (i**2, n):
                if j % i == 0:
                    L[j] = False
    return primos
