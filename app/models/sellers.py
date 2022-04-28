from unittest import skipUnless
from ..extensions import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func


class ProdutoPrecoGoogle(db.Model):
    __tablename__ = 'ProdutoPrecoGoogle'
    IdProdutoPreco = db.Column(db.Integer, primary_key=True, unique=True)
    EANGoogle = db.Column(db.String(), nullable=True, unique=False)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    IdProduto = db.Column(db.Integer, nullable=True, unique=False)
    IdMarca = db.Column(db.Integer, nullable=True, unique=False)
    SellerGoogle = db.Column(db.String(), nullable=True, unique=False)
    PrecoGoogle  = db.Column(db.Integer, nullable=True, unique=False)
    DataAtualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    UrlGoogle = db.Column(db.String(), nullable=True, unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    DataInserido = db.Column(DateTime(timezone=True), server_default=func.now())
    PerfilSeller = db.Column(db.String(), nullable=True, unique=False)

    def __init__(self,EANGoogle,SKU,IdProduto,IdMarca, SellerGoogle, PrecoGoogle, DataAtualizado,
                 UrlGoogle,bitAtivo,DataInserido,PerfilSeller):
        self.EANGoogle = EANGoogle
        self.SKU = SKU
        self.IdProduto = IdProduto
        self.IdMarca = IdMarca
        self.SellerGoogle = SellerGoogle
        self.PrecoGoogle = PrecoGoogle
        self.DataAtualizado = DataAtualizado
        self.UrlGoogle = UrlGoogle
        self.bitAtivo = bitAtivo
        self.DataInserido = DataInserido
        self.PerfilSeller = PerfilSeller


class InformacaoSeller():
    __tablename__ = 'InformacaoSeller'
    IdSeller = db.Column(db.Integer, primary_key=True, unique=True)
    Preco_Seller = db.Column(db.Integer, nullable=True, unique=False)
    PrecoCaixa = db.Column(db.Integer, nullable=True, unique=False)
    Imagem = db.Column(db.String(), nullable=True, unique=False)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    SKUHausz = db.Column(db.String(), nullable=True, unique=False)
    EAN = db.Column(db.String(), nullable=True, unique=False)
    LinkAnuncio = db.Column(db.String(), nullable=True, unique=False)
    Peso = db.Column(db.Integer, nullable=True, unique=False)
    Largura = db.Column(db.Integer, nullable=True, unique=False)
    ProdutoImg = db.Column(db.String(), nullable=True, unique=False)
    ProdutoCaracteristica = db.Column(db.String(), nullable=True, unique=False)
    ProdutoMarca = db.Column(db.String(), nullable=True, unique=False)
    ProdutoLinha = db.Column(db.String(), nullable=True, unique=False)
    DataAtualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,Preco_Seller,PrecoCaixa, Imagem, SKU,SKUHausz,EAN, LinkAnuncio,Peso
                    ,Largura,ProdutoImg, ProdutoCaracteristica,ProdutoMarca,ProdutoLinha,DataAtualizado, bitAtivo):
        self.Preco_Seller = Preco_Seller
        self.PrecoCaixa = PrecoCaixa
        self.Imagem = Imagem
        self.SKU = SKU
        self.SKUHausz = SKUHausz
        self.EAN = EAN
        self.LinkAnuncio = LinkAnuncio
        self.Peso = Peso
        self.Largura = Largura
        self.ProdutoImg = ProdutoImg
        self.ProdutoCaracteristica = ProdutoCaracteristica
        self.ProdutoMarca = ProdutoMarca
        self.ProdutoLinha = ProdutoLinha
        self.DataAtualizado = DataAtualizado
        self.bitAtivo = bitAtivo


#Criar Tabela e inserir informacoes dos ultimoscoletados
class GoogleMenorPreco(db.Model):
    __tablename__ = 'GoogleMenorPreco'
    idgoogle = db.Column(db.Integer, primary_key=True, unique=True)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    EAN = db.Column(db.String(), nullable=True, unique=False)
    URLGOOGLE = db.Column(db.String(), nullable=True, unique=False)
    URLPERFILSELLER = db.Column(db.String(), nullable=True, unique=False)
    DataAtualizado = db.Column(DateTime(timezone=True), server_default=func.now())
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,SKU,EAN,URLGOOGLE,URLPERFILSELLER, DataAtualizado, bitAtivo):
        self.SKU = SKU
        self.EAN = EAN
        self.URLGOOGLE = URLGOOGLE
        self.URLPERFILSELLER = URLPERFILSELLER
        self.DataAtualizado = DataAtualizado
        self.bitAtivo = bitAtivo
        




















