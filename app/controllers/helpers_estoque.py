from ..extensions import db
from ..models.produtos import ProdutoDetalhe, ProdutoBasico, MarcaProduto
from ..models.sellers import ProdutoPrecoGoogle



def consulta_estoque_fisico_hausz():
    query_estoquefisico = """
        SELECT  DISTINCT basico.[SKU],basico.EstoqueLocal,basico.[NomeProduto],basico.[EAN]
        ,basico.SaldoAtual,estoq.NomeEstoque,estoq.PrioridadeEstoque
            
        FROM [HauszMapa].[Produtos].[ProdutoBasico] basico
        join [HauszMapa].[Estoque].[Estoque] as estoq
        on estoq.IdEstoque = basico.EstoqueAtual
        where basico.EstoqueAtual in (1,5)
        """
    
    saldofisicohausz = db.engine.execute(query_estoquefisico).all()

    return saldofisicohausz
