from ..extensions import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class ProdutoPrazo(db.Model):
    __tablename__ = 'ProdutoPrazo'
    IdProdutoPrazo = db.Column(db.Integer, primary_key=True, unique=True)
    UF = db.Column(db.String(), nullable=True, unique=False)
    IdMarca = db.Column(db.Integer, nullable=True, unique=False)
    PrazoTransporte =  db.Column(db.Integer, nullable=True, unique=False)
    PrazoFabricacao = db.Column(db.Integer, nullable=True, unique=False)
    PrazoTotal = db.Column(db.Integer, nullable=True, unique=False)

    def __init__(self,UF,IdMarca,PrazoTransporte, PrazoFabricacao, PrazoTotal):
        self.UF = UF
        self.IdMarca = IdMarca
        self.PrazoTransporte = PrazoTransporte
        self.PrazoFabricacao = PrazoFabricacao
        self.PrazoTotal = PrazoTotal


class ProdutoPrazoProducFornec(db.Model):
    __tablename__ = 'ProdutoPrazoProducFornec'
    IdPrazos = db.Column(db.Integer, primary_key=True, unique=True)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    PrazoProducao = db.Column(db.Integer, nullable=True, unique=False)
    PrazoOperacional = db.Column(db.Integer, nullable=True, unique=False)
    PrazoFaturamento = db.Column(db.Integer, nullable=True, unique=False)
    PrazoTotal = db.Column(db.Integer, nullable=True, unique=False)
    def __init__(self,SKU,PrazoProducao,PrazoOperacional, PrazoFaturamento,PrazoTotal):
        self.SKU = SKU
        self.PrazoProducao = PrazoProducao
        self.PrazoOperacional = PrazoOperacional
        self.PrazoFaturamento = PrazoFaturamento
        self.PrazoTotal = PrazoTotal


class PrazosTransporte(db.Model):
    __tablename__ = 'PrazosTransporte'
    IdPrazosTransporte = db.Column(db.Integer, primary_key=True, unique=True)
    UF = db.Column(db.String(), nullable=True, unique=False)
    IdPraca = db.Column(db.Integer, nullable=True, unique=False)
    Prazo = db.Column(db.Integer, nullable=True, unique=False)
    
    def __init__(self,UF,IdPraca,Prazo):
        self.UF = UF
        self.IdPraca = IdPraca
        self.Prazo = Prazo











