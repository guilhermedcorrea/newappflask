from ..extensions import db,admin
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView

class MovimentacaoEstoque(db.Model):
    __tablename__ = 'MovimentacaoEstoque'
    __table_args__ = {"schema": "Estoque"}
    IdMovimentacaoEstoque = db.Column(db.Integer, primary_key=True, unique=True)
    IdTipoMovimentacao = db.Column(db.Integer, nullable=True, unique=False)
    TipoOperacao = db.Column(db.String(), nullable=True, unique=False)
    PedidoVenda = db.Column(db.String(), nullable=True, unique=False)
    PedidoCompra = db.Column(db.String(), nullable=True, unique=False)
    IdProduto = db.Column(db.Integer, nullable=True, unique=False)
    CodigoProduto = db.Column(db.String(), nullable=True, unique=False)
    Quantidade = db.Column(db.Integer, nullable=True, unique=False)
    Observacao = db.Column(db.String(), nullable=True, unique=False)
    IdUnidade = db.Column(db.Integer, nullable=True, unique=False)
    IdEstoque = db.Column(db.Integer, nullable=True, unique=False)
    Saldo = db.Column(db.Integer, nullable=True, unique=False)
    DataInserido = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,IdTipoMovimentacao,TipoOperacao, PedidoVenda,PedidoCompra,IdProduto, CodigoProduto,
            Quantidade,Observacao, IdUnidade,IdEstoque,Saldo, DataInserido):
        self.IdTipoMovimentacao = IdTipoMovimentacao
        self.TipoOperacao = TipoOperacao
        self.PedidoVenda = PedidoVenda
        self.PedidoCompra = PedidoCompra
        self.IdProduto = IdProduto
        self.CodigoProduto = CodigoProduto
        self.Quantidade = Quantidade
        self.Observacao = Observacao
        self.IdUnidade = IdUnidade
        self.IdEstoque = IdEstoque
        self.Saldo = Saldo
        self.DataInserido = DataInserido


class LogMovimentacaoEstoque(db.Model):
    __tablename__ = 'LogMovimentacaoEstoque'
    __table_args__ = {"schema": "Estoque"}
    IdLogMovimentacaoEstoque = db.Column(db.Integer, primary_key=True, unique=True)
    IdMovimentacaoEstoque = db.Column(db.Integer, nullable=True, unique=False)
    IdTipoMovimentacao = db.Column(db.Integer, nullable=True, unique=False)
    TipoOperacao = db.Column(db.String(), nullable=True, unique=False)
    PedidoVenda = db.Column(db.String(), nullable=True, unique=False)
    PedidoCompra = db.Column(db.String(), nullable=True, unique=False)
    IdProduto = db.Column(db.Integer, nullable=True, unique=False)
    CodigoProduto = db.Column(db.String(), nullable=True, unique=False)
    Quantidade = db.Column(db.Integer, nullable=True, unique=False)
    Observacao  = db.Column(db.String(), nullable=True, unique=False)
    IdUnidade = db.Column(db.Integer, nullable=True, unique=False)
    IdEstoque = db.Column(db.Integer, nullable=True, unique=False)
    Saldo = db.Column(db.Integer, nullable=True, unique=False)
    DataInserido = db.Column(DateTime(timezone=True), server_default=func.now())
    DataInseridoLog = db.Column(DateTime(timezone=True), server_default=func.now())
    UsuarioAlteracao = db.Column(db.String(), nullable=True, unique=False)

    def __init__(self,IdMovimentacaoEstoque, IdTipoMovimentacao,TipoOperacao,
            PedidoVenda,PedidoCompra,IdProduto, CodigoProduto,Quantidade,Observacao,IdUnidade, IdEstoque,Saldo, DataInserido,DataInseridoLog,UsuarioAlteracao):
        self.IdMovimentacaoEstoque = IdMovimentacaoEstoque
        self.IdTipoMovimentacao = IdTipoMovimentacao
        self.TipoOperacao  = TipoOperacao
        self.PedidoVenda = PedidoVenda
        self.PedidoCompra = PedidoCompra
        self.IdProduto = IdProduto
        self.CodigoProduto = CodigoProduto
        self.Quantidade = Quantidade
        self.Observacao = Observacao
        self.IdUnidade = IdUnidade
        self.IdEstoque = IdEstoque
        self.Saldo = Saldo
        self.DataInserido = DataInserido
        self.DataInseridoLog = DataInseridoLog
        self.UsuarioAlteracao = UsuarioAlteracao


class Estoque(db.Model):
    __tablename__ = 'Estoque'
    __table_args__ = {"schema": "Estoque"}
    IdEstoque = db.Column(db.Integer, primary_key=True, unique=True)
    NomeEstoque = db.Column(db.String(), nullable=True, unique=False)
    PrioridadeEstoque = db.Column(db.Integer, nullable=True, unique=False)
    PrazoAdicional = db.Column(db.Integer, nullable=True, unique=False)
    bitCrossDocking = db.Column(db.Boolean, nullable=True, unique=False)
    bitShowroom = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,NomeEstoque,PrioridadeEstoque,PrazoAdicional,bitCrossDocking,bitShowroom):
        self.NomeEstoque = NomeEstoque
        self.PrioridadeEstoque = PrioridadeEstoque
        self.PrazoAdicional = PrazoAdicional
        self.bitCrossDocking = bitCrossDocking
        self.bitShowroom = bitShowroom


class EstoqueView(ModelView):
    form_edit_rules = {'name'}
    column_searchable_list = ['name']
    edit_model = True

    column_filters = ['name']


admin.add_view(ModelView(Estoque, db.session))

