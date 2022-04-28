from ..extensions import db
from ..models.produtos import ProdutoDetalhe, ProdutoBasico, MarcaProduto
from ..models.sellers import ProdutoPrecoGoogle
from datetime import datetime


def selectiona_unidade():
    query_unidade ="""
        SELECT DISTINCT [Nome]
        FROM [HauszMapa].[Cadastro].[Unidade]
        """

    unidades = db.engine.execute(query_unidade).all()

    return unidades


def seleciona_periodos_pedido_loja():
    querydatapedido = """

    SELECT DISTINCT format([DataInserido], 'd', 'pt-BR') AS DATAPEDIDO
    FROM [HauszMapa].[Pedidos].[PedidoFlexy]
    
    """
    datapedido = db.engine.execute(querydatapedido).all()
    return datapedido


def filtra_vendas_dia_loja():

    diaatual = datetime.today().strftime('%d-%m-%Y')
    atual = str(diaatual).replace("-","/")
    queryvendalojadiario = """
    SELECT  DISTINCT un.Nome,pflexy.[IdPedidoFlexy],pflexy.[StatusPedido],pflexy.[IdUnidade],pflexy.[ValorTotal],format(pflexy.[DataInserido], 'd', 'pt-BR') AS DATAPEDIDO
    FROM [HauszMapa].[Pedidos].[PedidoFlexy] pflexy
    JOIN [HauszMapa].[Cadastro].[Unidade] as un 
    on un.IdUnidade = pflexy.IdUnidade
    WHERE format(pflexy.[DataInserido], 'd', 'pt-BR') IN ('19/03/2022')
    """#.format()
    datapedido = db.engine.execute(queryvendalojadiario).all()

    return datapedido

def venda_loja():
    queryloja = """
    
    SELECT  DISTINCT TOP (20) brand.Marca
    ,SUM(pflexy.[ValorTotal]) OVER (PARTITION BY brand.Marca  ) as total
    ,SUM(basico.SaldoAtual) OVER (PARTITION BY brand.Marca  ) as totalSALDO
    FROM [HauszMapa].[Pedidos].[PedidoFlexy] pflexy
    JOIN [HauszMapa].[Cadastro].[Unidade] as un 
    on un.IdUnidade = pflexy.IdUnidade
    join [HauszMapa].[Pedidos].[ItensFlexy] as iten
    on iten.CodigoPedido = pflexy.CodigoPedido
    JOIN [HauszMapa].[Produtos].[ProdutoBasico] as basico
    ON basico.SKU = iten.SKU
    join [Produtos].[Marca] as brand
    on brand.IdMarca = basico.IdMarca
    WHERE format(pflexy.DataInserido, 'd', 'pt-BR') BETWEEN  '01/03/2022' AND '19/03/2022' and pflexy.[StatusPedido] != 'cancelado'
    ORDER BY total DESC

    
    """

    vendalojames = db.engine.execute(queryloja).all()
    return vendalojames

def selecionamarca_mesatual(brand):
    queryvendamarca ="""
        SELECT  DISTINCT pflexy.CodigoPedido,brand.PedidoMinimo,brand.PrazoFabricacao,prazforn.PrazoFaturamento,prazforn.PrazoOperacional,prazforn.PrazoProducao,prazforn.PrazoTotal,basico.SaldoAtual,brand.Marca,basico.NomeProduto,basico.EstoqueAtual,basico.EstoqueLocal
        ,basico.IdMarca,un.Nome,pflexy.[IdPedidoFlexy],pflexy.[StatusPedido],pflexy.[IdUnidade],pflexy.[ValorTotal],PRAZOPROD.PrazoFabricacao,PRAZOPROD.PrazoTransporte,PRAZOPROD.PrazoTotal
        ,format(pflexy.DataInserido, 'd', 'pt-BR') as vendasku
        FROM [HauszMapa].[Pedidos].[PedidoFlexy] pflexy
        JOIN [HauszMapa].[Cadastro].[Unidade] as un 
        on un.IdUnidade = pflexy.IdUnidade
        join [HauszMapa].[Pedidos].[ItensFlexy] as iten
        on iten.CodigoPedido = pflexy.CodigoPedido
        JOIN [HauszMapa].[Produtos].[ProdutoBasico] as basico
        ON basico.SKU = iten.SKU
        join [Produtos].[Marca] as brand
        on brand.IdMarca = basico.IdMarca
        JOIN [HauszMapa].[Produtos].[ProdutoPrazo] AS PRAZOPROD
        on PRAZOPROD.IdMarca = brand.IdMarca
        join [HauszMapa].[Produtos].[ProdutoPrazoProducFornec] as prazforn
        on prazforn.SKU = basico.SKU
        WHERE format(pflexy.DataInserido, 'd', 'pt-BR') BETWEEN  '01/03/2022' AND '19/03/2022' and brand.Marca in ('{}')
            
        """.format(brand)

    vendamaerca = db.engine.execute(queryvendamarca).all()
    return vendamaerca


def filtrospedidos(brand):
    queryfiltro = """
    SELECT  DISTINCT pflexy.CodigoPedido,
    pflexy.[StatusPedido],un.Nome
    FROM [HauszMapa].[Pedidos].[PedidoFlexy] pflexy
    JOIN [HauszMapa].[Cadastro].[Unidade] as un 
    on un.IdUnidade = pflexy.IdUnidade
    join [HauszMapa].[Pedidos].[ItensFlexy] as iten
    on iten.CodigoPedido = pflexy.CodigoPedido
    JOIN [HauszMapa].[Produtos].[ProdutoBasico] as basico
    ON basico.SKU = iten.SKU
    join [Produtos].[Marca] as brand
    on brand.IdMarca = basico.IdMarca
    JOIN [HauszMapa].[Produtos].[ProdutoPrazo] AS PRAZOPROD
    on PRAZOPROD.IdMarca = brand.IdMarca
    join [HauszMapa].[Produtos].[ProdutoPrazoProducFornec] as prazforn
    on prazforn.SKU = basico.SKU
    WHERE format(pflexy.DataInserido, 'd', 'pt-BR') BETWEEN  '01/03/2022' AND '19/03/2022' and brand.Marca in ('{}')
    
    """.format(brand)
    
    vendamaerca = db.engine.execute(queryfiltro).all()
    return vendamaerca


def pedidocliente():
    pass


