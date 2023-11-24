# main.py

from supermercado import Supermercado

def main():
    supermercado = Supermercado()

    while True:
        print("\n====== Menu de Opções ======")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("5. Salvar dados em arquivo")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            supermercado.inserir_produto()
        elif opcao == "2":
            supermercado.excluir_produto()
        elif opcao == "3":
            supermercado.listar_produtos()
        elif opcao == "4":
            supermercado.consultar_preco()
        elif opcao == "5":
            supermercado.salvar_dados_em_arquivo()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
