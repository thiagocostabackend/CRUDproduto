from conexao import Conexao


class CRUDProduto:
    def inserir(self, nome, preco, id_categoria):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """INSERT INTO produto (
                 nome, preco, id_categoria) 
                 VALUES (%s, %s, %s)
             """
        cursor.execute(sql, (nome, preco, id_categoria))
        conexao.commit()
        cursor.close()
        conexao.close()

    # criar os outros métodos (listar, buscar_por_id, atualizar, excluir) aqui

    def listar(self):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, nome, preco, id_categoria FROM produto"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        # Converter Decimal para float
        return [(r[0], r[1], float(r[2]), r[3]) for r in resultados]

    def buscar_por_id(self, id):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = "SELECT id, nome, preco, id_categoria FROM produto WHERE id = %s"
        cursor.execute(sql, (id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexao.close()
        # Converter Decimal para float
        if resultado:
            return (resultado[0], resultado[1], float(resultado[2]), resultado[3])
        return resultado

    def atualizar(self, id, nome, preco, id_categoria):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = """UPDATE produto 
                 SET nome = %s, preco = %s, id_categoria = %s 
                 WHERE id = %s
             """
        cursor.execute(sql, (nome, preco, id_categoria, id))
        conexao.commit()
        cursor.close()
        conexao.close()

    def excluir(self, id):
        conexao = Conexao.conectar()
        cursor = conexao.cursor()
        sql = "DELETE FROM produto WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        cursor.close()
        conexao.close()
