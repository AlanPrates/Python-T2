# empregados.py

class Empregado:
    def __init__(self, nome, sobrenome, ano_nascimento, rg, ano_admissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
        self.rg = rg
        self.ano_admissao = ano_admissao
        self.salario = salario

def ler_dados_do_arquivo(nome_arquivo):
    lista_empregados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                nome = dados[0]
                sobrenome = dados[1]
                ano_nascimento = int(dados[2])
                rg = dados[3]
                ano_admissao = int(dados[4])
                salario = float(dados[5])
                empregado = Empregado(nome, sobrenome, ano_nascimento, rg, ano_admissao, salario)
                lista_empregados.append(empregado)
    except FileNotFoundError:
        pass
    return lista_empregados

def salvar_dados_em_arquivo(lista_empregados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for empregado in lista_empregados:
            linha = f"{empregado.nome},{empregado.sobrenome},{empregado.ano_nascimento},{empregado.rg},{empregado.ano_admissao},{empregado.salario}\n"
            arquivo.write(linha)

def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado.salario *= 1.1

def cadastrar_empregado():
    print("\nCadastrando novo empregado:")
    nome = input("Digite o nome do empregado: ")
    sobrenome = input("Digite o sobrenome do empregado: ")
    ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
    rg = input("Digite o RG do empregado: ")
    ano_admissao = int(input("Digite o ano de admissão do empregado: "))
    salario = float(input("Digite o salário do empregado: "))

    novo_empregado = Empregado(nome, sobrenome, ano_nascimento, rg, ano_admissao, salario)
    print(f"\nEmpregado cadastrado: {novo_empregado.nome} {novo_empregado.sobrenome}")
    return novo_empregado


def exibir_menu_empregados():
    return None