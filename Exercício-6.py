L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-1])  # Reverso
print(L[-1::])  # Último elemento
print(L[:-1:])  # Todos menos o último
print(L[::-2])  # Reverso pulando de 2 em 2
print(L[-2::])  # Últimos dois elementos
print(L[:-2:])  # Todos menos os dois últimos

# Determinar o signo do zodíaco chinês
ano_nascimento = int(input("Digite o ano de nascimento: "))
signos_chineses = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]
signo = signos_chineses[ano_nascimento % 12]
print(f"O signo do zodíaco chinês é: {signo}")
