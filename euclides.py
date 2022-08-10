def euclides(a,b):
    """Retorna mdc(a,b)"""
    dividendo = a
    divisor = b
    resto = dividendo % divisor
    while resto != 0:
        dividendo = b
        divisor = resto
        resto = dividendo % divisor
    return divisor

def euclides_estendido(a,b):
    """Retorna mdc(a,b) e coeficientes alfa, beta tais que a*alfa + b*beta = mdc(a,b)"""
    x_antigo, x_novo = 1, 0
    y_antigo, y_novo = 0, 1
    dividendo = a
    divisor = b
    resto = dividendo % divisor
    while resto != 0:
        quociente = dividendo // divisor
        dividendo, divisor = divisor, resto
        resto = dividendo % divisor
        x_antigo, x_novo = x_novo, x_antigo - quociente*x_novo
        y_antigo, y_novo = y_novo, y_antigo - quociente*y_novo
    return divisor, x_novo, y_novo
