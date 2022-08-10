# utf-8

# Pseudocódigo
# ------------
# Algoritmo: Square & Multiply

# Entrada: a, e, n \in IN
# Saída: Forma reduzida de a^e mod(n)

# Passo 1: Faça a <- r <- forma reduzida de a mod(n)
# Passo 2: Faça d_k, d_{k-1}, ..., d_1, d_0 <- expansão binária de e
# Passo 3: Faça i = k - 1;
# Passo 4: Enquanto i > 0:
# 		      Faça a <- forma reduzida de a^2 mod(n)
# 		      Se d_i = 1:
# 		        Faça a <- forma reduzida de a*r mod(n)
# 		      Faça i <- i - 1
# Passo 5: Retorne a

def expansao_binaria(x: int):
    """Recebe um inteiro  x  e retorna sua expansão biánria na forma de lista
    de strings, em que cada item é o caractere 0 ou 1.
    """
    return list(bin(x))[2:]

def square(x: int, n: int):
    """Faz o passo "square" do alg. square and multiply.
    """
    return (x * x) % n

def multiply(x: int, r: int, n: int):
    """Faz o passo "multiply" do alg. square and multiply.
    """
    return (x * r) % n

def square_multiply(a, e, n, verbose=False):
    """Recebe a, e, n \\in IN.
    Retorna a forma reduzida de a^e mod(n)

    Exemplos de uso:
    >>> square_multiply(3, 5, 7)
    5
    >>> square_multiply(13, 75, 9)
    1
    >>> square_multiply(345, 585, 587)
    114
    """
    if verbose: print(f"Vamos calcular {a}^{e} mod({n})", end="\n\n")
    a_original = a

    # Passo 1
    r = a % n
    if verbose: print(f"Lembre-se que {a} mod({n}) = a = {r}")
    a = r

    # Passo 2
    exp_binaria = expansao_binaria(e)
    if verbose: print(f"Expansão binária de {e} é {bin(e)}")

    # Passo 4
    for algarismo in exp_binaria[1:]: # Não temos porquê usar um contador (Passo 3)
        a = square(a, n)              # quando o Python nos fornece o laço for
        if verbose: print(f"(bit = {algarismo}) Square:   a = {a}")
        if algarismo == '1':
            a = multiply(a, r, n)
            if verbose: print(f"          Multiply: a = {a}")

    # Passo 5
    if verbose: print(f"\nLogo, a forma reduzida é: \n    {a_original}^{e} mod({n}) = {a}")
    return a

def testar():
    import random

    for _ in range(10**4):
        a = random.randint(3, 10**6)
        e = random.randint(1, 10**6)
        n = random.randint(1, 10**4)
        if pow(a, e, n) != square_multiply(a, e, n):
            print(f"Erro em {a}^{e} mod {n}")


if __name__ == "__main__":
    # Primeiro usando o testmod
    from doctest import testmod
    testmod()

    # E comparando com pow do python
    testar()

    argumentacao_termina = """ O algoritmo termina pois tem um número limitado 
    de passos e, no passo que contém um laço, tem uma quantidade pré determinada 
    e bem comportada de vezes que vai passar por esse laço.
    Isto é, o laço será repetido tantas vezes quanto for o tamanho (quantidade 
    de dígitos) do número e. Isso é finito.
    """

    argumentacao_correto = """ Acho que é válido ressaltar que os testes acima
    comparam a saída do algoritmo implementado com a saída esperada e eles 
    indicam que o algoritmo deve estar correto.
    Mas, num sentido mais matemático e preciso, a corretude do algoritmo vem do
    fato que calculamos a potência com um expoente em outra base, mas, no fundo, 
    isso pouco importa, pois o número é literalmente o mesmo independente da
    base. Além disso, graças às propriedades das potências em aritmética
    modular, temos a garantia que os números tratados são equivalentes em 
    módulo. Logo, não faz diferença calcular a potência e depois reduzir em
    módulo n ou ir calculando a forma reduzida enquanto se calcula a potência.
    Um detalhe é que entramos no loop (passo 4) avaliando a partir do segundo
    bit pois o primeiro foi calculado no passo 1 separadamente (ele não foi
    esquecido!). Isso pode ser feito sem problemas pois o algarismo mais 
    significativo em base 2 sempre será 1, caso contrário seria literalmente um
    zero à esquerda e não faria parte do número.
    """

    # item b)
    square_multiply(13, 75, 9, verbose=True)

    # Vamos calcular 13^75 mod(9)

    # Lembre-se que 13 mod(9) = a = 4
    # Expansão binária de 75 é 0b1001011
    # (bit = 0) Square:   a = 7
    # (bit = 0) Square:   a = 4
    # (bit = 1) Square:   a = 7
    #           Multiply: a = 1
    # (bit = 0) Square:   a = 1
    # (bit = 1) Square:   a = 1
    #           Multiply: a = 4
    # (bit = 1) Square:   a = 7
    #           Multiply: a = 1

    # Logo, a forma reduzida é:
    #     13^75 mod(9) = 1
