# supermercado.py

class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self):
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        if len(codigo) == 13 and codigo.isdigit() and nome[0].isupper() and preco >= 0:
            produto = {"codigo": codigo, "nome": nome, "preco": preco}
            self.produtos.append(produto)
            print("Produto inserido com sucesso.")
        else:
            print("Dados inválidos. Verifique as regras e tente novamente.")

    def excluir_produto(self):
        codigo = input("Digite o código do produto a ser excluído: ")

        for produto in self.produtos:
            if produto["codigo"] == codigo:
                self.produtos.remove(produto)
                print("Produto excluído com sucesso.")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        self.produtos.sort(key=lambda x: x["preco"])  # Ordena os produtos pelo preço

        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    def consultar_preco(self):
        codigo = input("Digite o código do produto para consultar o preço: ")

        for produto in self.produtos:
            if produto["codigo"] == codigo:
                print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
                return
        print("Produto não encontrado.")

    def salvar_dados_em_arquivo(self):
        nome_arquivo = input("Digite o nome do arquivo para salvar os dados: ")

        try:
            with open(nome_arquivo, "w") as arquivo:
                for produto in self.produtos:
                    linha = f"{produto['codigo']},{produto['nome']},{produto['preco']}\n"
                    arquivo.write(linha)
            print(f"Dados salvos com sucesso no arquivo {nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao salvar dados no arquivo: {e}")
