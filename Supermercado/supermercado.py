class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self):
        """
        Função para inserir um novo produto no supermercado.

        Exemplo de uso:
        >> supermercado = Supermercado()
        >> supermercado.inserir_produto()
        Digite o código do produto: 1234567890123
        Digite o nome do produto: Batata
        Digite o preço do produto: 3.6
        Produto inserido com sucesso.
        """
        codigo = input("Digite o código do produto: ")

        # Certifique-se de que o código tenha exatamente 13 caracteres
        if len(codigo) != 13:
            print("Código inválido. Deve ter exatamente 13 caracteres.")
            return

        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))

        # Validar o nome e o preço conforme as regras estabelecidas
        if nome[0].isupper() and preco >= 0:
            produto = {"codigo": codigo, "nome": nome, "preco": preco}
            self.produtos.append(produto)
            print("Produto inserido com sucesso.")
        else:
            print("Dados inválidos. Verifique as regras e tente novamente.")

    def excluir_produto(self):
        codigo = input("Digite o código do produto a ser excluído: ")

        # Implemente a lógica para excluir o produto com o código informado
        for produto in self.produtos:
            if produto["codigo"] == codigo:
                self.produtos.remove(produto)
                print("Produto excluído com sucesso.")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        # Implemente a lógica para listar todos os produtos
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    def consultar_preco(self):
        # Implemente a lógica para consultar o preço de um produto
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
