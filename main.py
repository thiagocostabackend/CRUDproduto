from crudproduto import CRUDProduto

class SistemaProduto:
    def __init__(self):
        self.crud_produto = CRUDProduto()

    def executar(self):
        while True:
            print("\n--- MENU ---")
            print("1 - Inserir Produto")
            print("2 - Listar produtos")
            print("3 - Buscar produto")
            print("4 - Atualizar produto")
            print("5 - Excluir produto")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome do Produto: ")
                preco = float(input("Preço do Produto: "))
                id_categoria = int(input("ID da Categoria: "))
                self.crud_produto.inserir(nome, preco, id_categoria)
                print("Produto inserido com sucesso!")

            elif opcao == "2":
                produtos = self.crud_produto.listar()
                for produto in produtos:
                    print(produto)

            elif opcao == "3":
                id_produto = int(input("ID do Produto a buscar: "))
                produto = self.crud_produto.buscar(id_produto)
                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado.")

            elif opcao == "4":
                id_produto = int(input("ID do Produto a atualizar: "))
                nome = input("Novo nome do Produto: ")
                preco = float(input("Novo preço do Produto: "))
                id_categoria = int(input("Novo ID da Categoria: "))
                atualizado = self.crud_produto.atualizar(id_produto, nome, preco, id_categoria)
                if atualizado:
                    print("Produto atualizado com sucesso!")
                else:
                    print("Produto não encontrado.")

            elif opcao == "5":
                id_produto = int(input("ID do Produto a excluir: "))
                excluido = self.crud_produto.excluir(id_produto)
                if excluido:
                    print("Produto excluído com sucesso!")
                else:
                    print("Produto não encontrado.")
            elif opcao == "0":
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

            

if __name__ == "__main__":
        sistema = SistemaProduto()
        sistema.executar()