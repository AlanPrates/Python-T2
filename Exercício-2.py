# Parte 1: Demonstração dos operadores aritméticos em Python
a = 5
b = 2

# Operadores aritméticos
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# Operadores aritméticos compostos
a += 1  # equivalente a a = a + 1
b *= 2  # equivalente a b = b * 2

# Parte 2: Demonstração da representação de números inteiros grandes
fatorial_30 = 30 * 29 * 28 * 27 * 26 * 25 * 24 * 23 * 22 * 21 * 20 * 19 * 18 * 17 * 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

# Maior valor inteiro representável em C/C++
max_int_c = 2**31 - 1

# Parte 3: Variáveis numéricas são imutáveis
num1 = 10
num2 = num1
num1 += 5

# Verificando os métodos disponíveis para variáveis inteiras
print(dir(int))
