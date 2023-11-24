# main.py

from supermercado import Supermercado
from empregados import ler_dados_do_arquivo, exibir_menu_empregados, salvar_dados_em_arquivo, reajusta_dez_porcento, cadastrar_empregado

def main():
    supermercado = Supermercado()
    lista_empregados = ler_dados_do_arquivo("dados_empregados.txt")

    while True:
        print("\n====== Menu Principal ======")
        print("1. Supermercado")
        print("2. Empregados")
        print("0. Sair")

        opcao_principal = input("Digite a opção desejada: ")

        if opcao_principal == "1":
            # Menu do Supermercado
            while True:
                print("\n====== Menu Supermercado ======")
                print("1. Inserir um novo produto")
                print("2. Excluir um produto cadastrado")
                print("3. Listar todos os produtos")
                print("4. Consultar o preço de um produto")
                print("5. Salvar dados em arquivo (Supermercado)")
                print("0. Voltar para o menu principal")

                opcao_supermercado = input("Digite a opção desejada: ")

                if opcao_supermercado == "1":
                    supermercado.inserir_produto()
                elif opcao_supermercado == "2":
                    supermercado.excluir_produto()
                elif opcao_supermercado == "3":
                    supermercado.listar_produtos()
                elif opcao_supermercado == "4":
                    supermercado.consultar_preco()
                elif opcao_supermercado == "5":
                    supermercado.salvar_dados_em_arquivo()
                elif opcao_supermercado == "0":
                    print("Voltando para o menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao_principal == "2":
            # Menu dos Empregados
            while True:
                print("\n====== Menu Empregados ======")
                print("1. Reajustar salários em 10%")
                print("2. Listar salários dos empregados")
                print("3. Cadastrar novo empregado")
                print("4. Salvar dados em arquivo (Empregados)")
                print("0. Voltar para o menu principal")

                opcao_empregados = input("Digite a opção desejada: ")

                if opcao_empregados == "1":
                    reajusta_dez_porcento(lista_empregados)
                    print("Salários reajustados em 10%.")
                elif opcao_empregados == "2":
                    for empregado in lista_empregados:
                        print(f"{empregado.nome} {empregado.sobrenome}: R${empregado.salario:.2f}")
                elif opcao_empregados == "3":
                    try:
                        novo_empregado = cadastrar_empregado()
                        lista_empregados.append(novo_empregado)
                        print("Empregado cadastrado com sucesso.")
                    except ValueError as e:
                        print(f"Erro ao cadastrar empregado: {e}")
                elif opcao_empregados == "4":
                    salvar_dados_em_arquivo(lista_empregados, "dados_empregados.txt")
                    print("Dados dos empregados salvos com sucesso.")
                elif opcao_empregados == "0":
                    print("Voltando para o menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao_principal == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
