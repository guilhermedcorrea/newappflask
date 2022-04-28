from ..extensions import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


class ProdutoPreco(db.Model):
    __tablename__ = 'ProdutoPreco'
    IdPrecoBase = db.Column(db.Integer, primary_key=True, unique=True)
    IdProduto = db.Column(db.Integer, nullable=True, unique=False)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    Custo = db.Column(db.Integer, nullable=True, unique=False)
    PrecoBase = db.Column(db.Integer, nullable=True, unique=False)
    PrecoFrete = db.Column(db.Integer, nullable=True, unique=False)
    Preco = db.Column(db.Integer, nullable=True, unique=False)
    IdUnidade = db.Column(db.Integer, nullable=True, unique=False)
    AlteradoPor = db.Column(db.String(), nullable=True, unique=False)
    DataAlteracao = db.Column(DateTime(timezone=True), server_default=func.now())
    IdEstoque = db.Column(db.Integer, nullable=True, unique=False)
    IdMarkup = db.Column(db.Integer, nullable=True, unique=False)

    def __init__(self,IdProduto, SKU,Custo,PrecoBase, PrecoFrete , Preco,IdUnidade,
                AlteradoPor, DataAlteracao,IdEstoque,IdMarkup):
        self.IdProduto = IdProduto
        self.SKU = SKU
        self.Custo = Custo
        self.PrecoBase = PrecoBase
        self.PrecoFrete = PrecoFrete
        self.Preco = Preco
        self.IdUnidade = IdUnidade
        self.AlteradoPor = AlteradoPor
        self.DataAlteracao = DataAlteracao
        self.IdEstoque = IdEstoque
        self.IdMarkup = IdMarkup


class ProdutoPrecoFrete(db.Model):
    __tablename__ = 'ProdutoPrecoFrete'
    IdPreco = db.Column(db.Integer, primary_key=True, unique=True)
    IdProduto = db.Column(db.Integer, nullable=True, unique=False)
    IdUnidade = db.Column(db.Integer, nullable=True, unique=False)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    Custo = db.Column(db.Integer, nullable=True, unique=False)
    CustoFrete = db.Column(db.Integer, nullable=True, unique=False)
    PrecoVista = db.Column(db.Integer, nullable=True, unique=False)
    PrecoSugerido =  db.Column(db.Integer, nullable=True, unique=False)
    DataInserido = db.Column(DateTime(timezone=True), server_default=func.now())
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    InseridoPor = db.Column(db.String(), nullable=True, unique=False)
    IdEstoque = db.Column(db.Integer, nullable=True, unique=False)
    IdMarkup = db.Column(db.Integer, nullable=True, unique=False)
    Margem = db.Column(db.Integer, nullable=True, unique=False)

    def __init__(self,IdProduto, IdUnidade,SKU,Custo,  CustoFrete, PrecoVista,
        PrecoSugerido, bitAtivo, InseridoPor,IdEstoque,IdMarkup, Margem):
        self.IdProduto = IdProduto
        self.IdUnidade = IdUnidade
        self.SKU = SKU
        self.Custo = Custo
        self.CustoFrete = CustoFrete
        self.PrecoVista = PrecoVista
        self.PrecoSugerido = PrecoSugerido
        self.bitAtivo = bitAtivo
        self.InseridoPor = InseridoPor
        self.IdEstoque = IdEstoque
        self.IdMarkup = IdMarkup
        self.Margem = Margem


class ProdutoPrecoBase(db.Model):
    __tablename__ = 'ProdutoPrecoBase'
    IdProdutoBase = db.Column(db.Integer, primary_key=True, unique=True)
    IdProduto =  db.Column(db.Integer, nullable=True, unique=False)
    Sku = db.Column(db.String(), nullable=True, unique=False)
    IdEstoque =  db.Column(db.Integer, nullable=True, unique=False)
    Custo = db.Column(db.Integer, nullable=True, unique=False)
    Preco = db.Column(db.Integer, nullable=True, unique=False)
    MarkupVenda =  db.Column(db.Integer, nullable=True, unique=False)
    MarkupEcommerce =  db.Column(db.Integer, nullable=True, unique=False)
    MarkupCNPJ = db.Column(db.Integer, nullable=True, unique=False)
    MarkupEasy = db.Column(db.Integer, nullable=True, unique=False)
    AlteradoPor = db.Column(db.String(), nullable=True, unique=False)
    DataAlteracao = db.Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self,IdProduto, Sku, IdEstoque,Custo,Preco, MarkupVenda, MarkupEcommerce,
                MarkupCNPJ, MarkupEasy, AlteradoPor,DataAlteracao):
        self.IdProduto = IdProduto
        self.Sku = Sku
        self.IdEstoque = IdEstoque
        self.Custo = Custo
        self.Preco = Preco
        self.MarkupVenda = MarkupVenda
        self.MarkupEcommerce = MarkupEcommerce
        self.MarkupCNPJ = MarkupCNPJ
        self.MarkupEasy = MarkupEasy
        self.AlteradoPor = AlteradoPor
        self.DataAlteracao = DataAlteracao











        


