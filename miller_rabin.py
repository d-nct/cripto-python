# utf-8
from random import randint

def teste_de_miller(p, b):
    """p>2 ímpar e b inteiro tal que b != 0 em IZ_p

    Retorno 
    -------
        True se p é composto
        False se teste inconclusivo

    Exemplos
    --------
    >>> teste_de_miller(27, 2)
    True
    >>> teste_de_miller(25, 7)
    False
    >>> teste_de_miller(25, 2)
    True
    """
    def calcula_q_k(n):
        q = n - 1
        k = 0
        while True:
            if q // 2 != q / 2:
                return q, k
            q = q // 2
            k += 1

    # "Passo 0": Checagens
    if (p % 2) == 0: return True

    # Para entendermos melhor
    menos_um = p - 1

    # Passo 1
    q, k = calcula_q_k(p)

    # Passo 2
    chute = pow(b, q, p)
    if chute == 1 or chute == menos_um:
        return False

    # Passo 3
    contador = 1
    while contador < k:
        chute = pow(chute, 2, p)
        if chute == 1: return True
        if chute == menos_um: return False
        contador += 1
    
    # Passo 4
    return True

def teste_de_miller_rabin(p, num_iter=10):
    """Testa p com Miller-Rabin e bases aleatórias

    Retorno
    -------
      True  se p é composto
      False se p é primo (provavelmente)

    Notas
    -----
      Teorema de Rabin: Teste de Miller acerta em 3/4 das bases entre 2 e p-2.
      Então, 10 iterações é suficiente para a resposta ser precisa.
    """
    for _ in range(num_iter):
        # escolhendo uma base
        base = 0
        while (base % p) == 0: 
            base = randint(0, 10**4)

        if teste_de_miller(p, base):
            return True

    return False




if __name__ == "__main__":
    # Primeiro usando o testmod
    from doctest import testmod
    testmod()
