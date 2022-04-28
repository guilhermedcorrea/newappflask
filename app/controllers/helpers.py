from ..extensions import db
from ..models.produtos import ProdutoDetalhe, ProdutoBasico, MarcaProduto
from ..models.sellers import ProdutoPrecoGoogle


def filtrar_subcategorias():

    query_subcategorias = """
            SELECT  distinct detalhe.[IdSubCat]	,sub.NomeSubCat
            FROM [HauszMapa].[Produtos].[ProdutoDetalhe] detalhe
            join [Produtos].[Marca] as brand
            on brand.IdMarca = detalhe.IdMarca
            join [Produtos].[SubCategoria] as sub
            on sub.IdSubCat = detalhe.IdSubCat
            """

    subcat = db.engine.execute(query_subcategorias).all()

   
    return subcat


def filtrar_categorias():
    query_categorias = """
        SELECT  distinct cat.IdCat,cat.NomeCat
        FROM [HauszMapa].[Produtos].[ProdutoDetalhe] detalhe
        join [Produtos].[Marca] as brand
        on brand.IdMarca = detalhe.IdMarca
        join [Produtos].[SubCategoria] as sub
        on sub.IdSubCat = detalhe.IdSubCat
        join [HauszMapa].[Produtos].[Categoria] as cat
        on cat.IdCat = sub.IdCat
    
        """
    categorias = db.engine.execute(query_categorias).all()

    return categorias


def filtrar_departamentos():
    query_departamento = """
        SELECT  distinct dept.IdDept,dept.NomeDept
        FROM [HauszMapa].[Produtos].[ProdutoDetalhe] detalhe
        join [Produtos].[Marca] as brand
        on brand.IdMarca = detalhe.IdMarca
        join [Produtos].[SubCategoria] as sub
        on sub.IdSubCat = detalhe.IdSubCat
        join [HauszMapa].[Produtos].[Categoria] as cat
        on cat.IdCat = sub.IdCat
        join [Produtos].[Departamento] as dept
        on dept.IdDept = cat.IdDept
        
        """
    departamentos = db.engine.execute(query_departamento).all()

    return departamentos


def filtrar_marcas():
    querymarcas = """
        SELECT  distinct brand.IdMarca,brand.Marca
        FROM [HauszMapa].[Produtos].[ProdutoDetalhe] detalhe
        join [Produtos].[Marca] as brand
        on brand.IdMarca = detalhe.IdMarca
    
        """
    marcas = db.engine.execute(querymarcas).all()

    return marcas