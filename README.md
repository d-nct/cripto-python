# Objetivos

Esse repositório existe para armazenar algumas implementações de algoritmos vistos
durante as aulas de Números Inteiros e Criptografia, disciplina obrigatória do
curso de Bacharelado em Ciência da Computação na UFRJ.

# Algoritmos

## Algoritmo de Euclides

Calcula o `mdc` entre dois números.

## Algoritmo de Euclides Estendido

Calcula o `mdc` entre dois números `a` e `b` e os coeficientes do Teorema de Bézout associado
a eles. Isto é, calcula o `mdc`, `alfa` e `beta` tais que 
```python
mdc(a,b) = a * alfa + b * beta
```

## Crivo de Erastótenes

Encontra todos os números primos de 0 até um determinado número.

## Teste de Miller

Usa o Pequeno Teorema de Fermat para testar se um número `p` é composto usando
uma certa base `b`.

## Teste de Miller-Rabin

Aplica o Teste de Miller iteradamente, pois Rabin provou que, se `n` é composto,
 então o Teste de Miller acerta para 3/4 das bases.

## Square and Multiply

Algoritmo utilizado para o cálculo de potências em módulo `n` de forma mais eficiente.

## RSA (Ingênua)

Depois de 6 meses para entender o algoritmo, eis a implementação em python, utilizando
boa parte dos demais recursos vistos em aula.

O programa é capaz de encriptar e descriptar mensagens utilizando RSA, mas cuidado, pois
a implementação não tem a malandragem das ruas que a RSA da biblioteca vai ter! Isto
é, é bem possível que ela será fácilmente quebrada.
