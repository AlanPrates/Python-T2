# Parte 1: Manipulação de strings
nome_completo = "Seu Nome Completo"
nome, sobrenome = nome_completo.split()

# Verificar ordem alfabética
ordem_alfabetica = sorted([nome, sobrenome])

# Verificar quantidade de caracteres
len_nome = len(nome)
len_sobrenome = len(sobrenome)

# Verificar se é palíndromo
e_palindromo = nome_completo == nome_completo[::-1]

# Parte 2: Exibir resultados
print(f"Nome: {nome}, Sobrenome: {sobrenome}")
print(f"Ordem alfabética: {ordem_alfabetica}")
print(f"Quantidade de caracteres - Nome: {len_nome}, Sobrenome: {len_sobrenome}")
print(f"É palíndromo: {e_palindromo}")
