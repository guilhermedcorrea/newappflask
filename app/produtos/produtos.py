from flask import Blueprint, render_template, redirect,url_for
from ..extensions import db
from ..models.produtos import ProdutoDetalhe, ProdutoBasico, MarcaProduto
from ..models.sellers import ProdutoPrecoGoogle
from ..controllers.helpers import filtrar_subcategorias,filtrar_categorias,filtrar_departamentos,filtrar_marcas
from ..controllers.helpers_produtos import consulta_skus

#Inicializa Blueprint
produtos = Blueprint('produtos', __name__,template_folder='templates',static_folder='static',static_url_path='/static/')

@produtos.route("/produtos",methods=['GET','POST'])
@produtos.route("/produtos/<int:page>",methods=['GET','POST'])
def retornaprodutos(page=1):
    queryprodutos = """
        DECLARE @PageNumber AS INT
        DECLARE @RowsOfPage AS INT
        SET @PageNumber= {}
        SET @RowsOfPage= 8
        SELECT basico.[IdProduto],basico.[SKU],basico.[NomeProduto] ,basico.[EAN]
        ,basico.[bitLinha],basico.[BitAtivo],detalhe.[Descricao],detalhe.[TamanhoBarra],detalhe.[Unidade]
        ,detalhe.[FatorVenda],detalhe.[FatorMultiplicador],detalhe.[FatorUnitario],detalhe.[UrlImagem],detalhe.[Garantia],detalhe.[Comprimento],detalhe.[Largura]
        ,detalhe.[Altura],detalhe.[ValorMinimo],detalhe.[bitVerificadoFoto],detalhe.[Peso],detalhe.[bitAtivo],
        brand.Marca,sub.NomeSubCat,cat.NomeCat,dpt.NomeDept
        FROM [HauszMapa].[Produtos].[ProdutoBasico] as basico
        join [HauszMapa].[Produtos].[ProdutoDetalhe] as detalhe
        on detalhe.IdProduto = basico.IdProduto
        join [Produtos].[Marca] as brand
        on brand.IdMarca = basico.IdMarca
        join [Produtos].[SubCategoria] as sub
        on sub.IdSubCat = basico.IdSubCat
        join [Produtos].[Categoria] as cat
        on cat.IdCat = sub.IdCat
        join [Produtos].[Departamento]  as dpt
        on dpt.IdDept = cat.IdDept
        order by basico.[IdProduto]
        OFFSET (@PageNumber-1)*@RowsOfPage ROWS
        FETCH NEXT @RowsOfPage ROWS ONLY

        """.format(page)
    produtos = db.engine.execute(queryprodutos).all()


    return render_template("produtos.html",page=page,produtos=produtos )
