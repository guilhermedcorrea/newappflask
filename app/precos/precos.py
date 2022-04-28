from flask import Blueprint, render_template, redirect,url_for, request
from ..extensions import db
from ..models.produtos import ProdutoDetalhe, ProdutoBasico, MarcaProduto
from ..models.sellers import ProdutoPrecoGoogle
from ..controllers.helpers import filtrar_subcategorias,filtrar_categorias,filtrar_departamentos,filtrar_marcas
from ..models.forms import Selectfiledform

#Inicializa Blueprint
precos = Blueprint('precos', __name__,template_folder='templates',static_folder='static',static_url_path='/static/')

@precos.route("/precos")
@precos.route("/precos/<int:page>",methods=['GET','POST'])
def indexprecos(page=1):
 
    query ="""
    DECLARE @PageNumber AS INT
    DECLARE @RowsOfPage AS INT
    SET @PageNumber= {}
    SET @RowsOfPage= 8

    SELECT DISTINCT produto.IdProduto,produto.[SKU],brand.Marca,produto.[NomeProduto],produto.[EAN]
    ,google.UrlGoogle,prec.Custo, prec.Preco,PDT.UrlImagem,PDT.[FatorMultiplicador],produto.SaldoAtual,estoq.NomeEstoque,estoq.PrazoAdicional
    ,estoq.PrioridadeEstoque,prazoforn.PrazoFaturamento,prazoforn.PrazoOperacional,prazoforn.PrazoProducao,prazoforn.PrazoTotal
    ,fornmarc.PedidoMinimo,fornmarc.PrazoFabricacao
                                    
    ,max(format(google.DataInserido, 'd', 'pt-BR')) OVER (PARTITION BY google.SellerGoogle) as dataatualizado
    ,(
    SELECT Tab.Minp FROM (
    SELECT MIN(PrecoGoogle) Minp, EANGoogle FROM [HauszMapaDev2].[Produtos].[ProdutoPrecoGoogle] WHERE EANGoogle = produto.EAN GROUP BY EANGoogle)Tab) MinP
    ,
    (
                            
    SELECT TOP 1 SellerGoogle FROM [HauszMapaDev2].[Produtos].[ProdutoPrecoGoogle] WHERE EANGoogle = produto.EAN
    AND PrecoGoogle = 
    (SELECT Tab2.Minp FROM (
    (SELECT MIN(PrecoGoogle) Minp, EANGoogle FROM [HauszMapaDev2].[Produtos].[ProdutoPrecoGoogle] WHERE EANGoogle = produto.EAN GROUP BY EANGoogle)
    )Tab2 
                            
    ) 
    )
                            
    FROM [HauszMapa].[Produtos].[ProdutoBasico] as produto
    join [HauszMapaDev2].[Produtos].[ProdutoPrecoGoogle] as google
    on google.EANGoogle = produto.EAN
    JOIN Produtos.Marca as brand
    on brand.IdMarca = produto.IdMarca
    join [Produtos].[ProdutoPreco] as prec
    on prec.IdProduto = produto.IdProduto
    JOIN Produtos.EspecificacaoProdutos as esp
    on esp.SKU = produto.SKU
    JOIN [Produtos].[ProdutoDetalhe] AS PDT
    ON PDT.IdProduto = produto.IdProduto
    join [HauszMapa].[Estoque].[Estoque] as estoq
    on estoq.IdEstoque = produto.EstoqueAtual
    join [HauszMapa].[Produtos].[ProdutoPrazoProducFornec] as prazoforn
    on prazoforn.SKU = produto.SKU
    join [HauszMapa].[Produtos].[FornecedorMarca] as fornmarc
    on fornmarc.IdMarca = brand.IdMarca
    WHERE prec.IdUnidade = 1
    order by produto.IdProduto asc
    OFFSET (@PageNumber-1)*@RowsOfPage ROWS
    FETCH NEXT @RowsOfPage ROWS ONLY
                
   
    """.format(page)
    produtos = db.engine.execute(query).all()

    subcategorias = filtrar_subcategorias()
    categorias = filtrar_categorias()

    departamentos = filtrar_departamentos()
 
    marcas = filtrar_marcas()
    if request.method == 'POST':
      
        departamento = request.form['departamento']
        categoria = request.form['categoria']
        sbcategoria = request.form['subcategoria']
        print(departamento, categoria,sbcategoria)

 
        
    return render_template("precos.html",page=page,produtos=produtos,subcategorias=subcategorias,
    categorias=categorias,departamentos=departamentos,marcas=marcas)

@precos.route("/sku/<int:value>", methods=['GET', 'POST'])
def sku(value):
    query = """ select  *from produtos where id_vtex = {}""".format(value)
    produto = db.engine.execute(query).first()
    
    print(produto)

    return render_template('lista.html',produtos=produto)
