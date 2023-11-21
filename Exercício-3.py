# Parte 1: Imprimir caracteres numéricos e seus códigos ASCII
for i in range(10):
    print(f"'{i}' - {ord(str(i))}")

# Modificar para imprimir em octal e hexadecimal
for i in range(10):
    print(f"'{i}' - {ord(str(i))} - Octal: {oct(ord(str(i)))} - Hexadecimal: {hex(ord(str(i)))}")

# Adicionar a leitura de um caractere da entrada padrão
caractere = input("Digite um caractere: ")
print(f"'{caractere}' - {ord(caractere)} - Octal: {oct(ord(caractere))} - Hexadecimal: {hex(ord(caractere))}")

# Trabalhar com caracteres especiais
caractere_especial = 'ç'
print(f"'{caractere_especial}' - {ord(caractere_especial)} - Octal: {oct(ord(caractere_especial))} - Hexadecimal: {hex(ord(caractere_especial))}")
