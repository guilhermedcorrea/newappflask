from ..extensions import db
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func

class ProdutoBasico():
    __tablename__ = 'ProdutoBasico'
    IdProduto = db.Column(db.Integer, primary_key=True, unique=True)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    CodOmie = db.Column(db.String(), nullable=True, unique=False)
    NomeProduto = db.Column(db.String(), nullable=True, unique=False)
    NomeEtiqueta = db.Column(db.String(), nullable=True, unique=False)
    NomeTotem = db.Column(db.String(), nullable=True, unique=False)
    EAN = db.Column(db.String(), nullable=True, unique=False)
    NCM = db.Column(db.String(), nullable=True, unique=False)
    CEST = db.Column(db.String(), nullable=True, unique=False)
    DataInserido = db.Column(db.String(), nullable=True, unique=False)
    IdMarca = db.Column(db.Integer, nullable=True, unique=False)
    ValorMinimo = db.Column(db.Integer, nullable=True, unique=False)
    bitLinha = db.Column(db.Boolean, nullable=True, unique=False)
    BitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    IdSubCat = db.Column(db.Integer, nullable=True, unique=False)
    bitOmie = db.Column(db.Boolean, nullable=True, unique=False)
    EstoqueAtual = db.Column(db.Integer, nullable=True, unique=False)
    SaldoAtual = db.Column(db.Integer, nullable=True, unique=False)
    InseridoPor = db.Column(db.String(), nullable=True, unique=False)
    DataAlteracao = db.Column(DateTime(timezone=True), server_default=func.now())
    bitPromocao =  db.Column(db.Boolean, nullable=True, unique=False)
    bitAtualizadoPreco = db.Column(db.Boolean, nullable=True, unique=False)
    bitPrecoAtualizado = db.Column(db.Boolean, nullable=True, unique=False)
    PesoCubado =  db.Column(db.Integer, nullable=True, unique=False)
    Peso = db.Column(db.Integer, nullable=True, unique=False)
    IdDept = db.Column(db.Integer, nullable=True, unique=False)
    EstoqueLocal = db.Column(db.String(), nullable=True, unique=False)
    bitEasy = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,SKU, CodOmie, NomeProduto,NomeEtiqueta, NomeTotem,EAN,NCM, CEST,DataInserido,IdMarca,
        ValorMinimo, bitLinha, BitAtivo, IdSubCat, bitOmie, EstoqueAtual,SaldoAtual, InseridoPor, DataAlteracao,
        bitPromocao, bitAtualizadoPreco,bitPrecoAtualizado,PesoCubado,Peso,IdDept, EstoqueLocal,bitEasy):
        self.SKU = SKU
        self.CodOmie = CodOmie
        self.NomeProduto = NomeProduto
        self.NomeEtiqueta = NomeEtiqueta
        self.NomeTotem = NomeTotem
        self.EAN = EAN
        self.NCM = NCM
        self.CEST = CEST
        self.DataInserido = DataInserido
        self.IdMarca = IdMarca
        self.ValorMinimo = ValorMinimo
        self.bitLinha = bitLinha
        self.BitAtivo = BitAtivo
        self.IdSubCat = IdSubCat
        self.bitOmie = bitOmie
        self.EstoqueAtual = EstoqueAtual
        self.SaldoAtual = SaldoAtual
        self.InseridoPor = InseridoPor
        self.DataAlteracao = DataAlteracao
        self.bitPromocao = bitPromocao
        self.bitAtualizadoPreco = bitAtualizadoPreco
        self.bitPrecoAtualizado = bitPrecoAtualizado
        self.PesoCubado = PesoCubado
        self.Peso = Peso
        self.IdDept = IdDept
        self.EstoqueLocal = EstoqueLocal
        self.bitEasy = bitEasy


class ProdutoDetalhe(db.Model):
    __tablename__ = 'ProdutoDetalhe'
    IdProduto = db.Column(db.Integer, primary_key=True, unique=True)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    IdMarca = db.Column(db.Integer, nullable=True, unique=False)
    IdSubCat =  db.Column(db.Integer, nullable=True, unique=False)
    Descricao = db.Column(db.String(), nullable=True, unique=False)
    QuantidadeMinima = db.Column(db.Integer, nullable=True, unique=False)
    TamanhoBarra = db.Column(db.String(), nullable=True, unique=False)
    Unidade = db.Column(db.Integer, nullable=True, unique=False)
    FatorVenda = db.Column(db.Integer, nullable=True, unique=False)
    FatorMultiplicador = db.Column(db.Integer, nullable=True, unique=False)
    FatorUnitario = db.Column(db.String(), nullable=True, unique=False)
    UrlImagem = db.Column(db.String(), nullable=True, unique=False)
    Garantia = db.Column(db.String(), nullable=True, unique=False)
    Nimagem = db.Column(db.Integer, nullable=True, unique=False)
    Comprimento = db.Column(db.Integer, nullable=True, unique=False)
    Largura = db.Column(db.Integer, nullable=True, unique=False)
    Altura = db.Column(db.Integer, nullable=True, unique=False)
    ValorMinimo = db.Column(db.Integer, nullable=True, unique=False)
    bitVerificadoFoto = db.Column(db.Boolean, nullable=True, unique=False)
    Peso = db.Column(db.Integer, nullable=True, unique=False)
    bitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    UsuarioAlteracao = db.Column(db.String(), nullable=True, unique=False)
    DataInserido = db.Column(DateTime(timezone=True), server_default=func.now())
    IdProdutoNaoUsaMais = db.Column(db.Integer, nullable=True, unique=False)
    

    def __init__(self,SKU,IdMarca, IdSubCat, Descricao, QuantidadeMinima,TamanhoBarra, Unidade
        ,FatorVenda,FatorMultiplicador, FatorUnitario,UrlImagem,Garantia,Nimagem,Comprimento, Largura
        ,ValorMinimo,bitVerificadoFoto,Peso,bitAtivo,UsuarioAlteracao,DataInserido,IdProdutoNaoUsaMais):
        self.SKU = SKU
        self.IdMarca = IdMarca
        self.IdSubCat = IdSubCat
        self.Descricao = Descricao
        self.QuantidadeMinima = QuantidadeMinima
        self.TamanhoBarra = TamanhoBarra
        self.Unidade = Unidade
        self.FatorVenda = FatorVenda
        self.FatorMultiplicador = FatorMultiplicador
        self.FatorUnitario = FatorUnitario
        self.UrlImagem = UrlImagem
        self.Garantia = Garantia
        self.Nimagem = Nimagem
        self.Comprimento = Comprimento
        self.Largura = Largura
        self.ValorMinimo = ValorMinimo
        self.bitVerificadoFoto = bitVerificadoFoto
        self.Peso = Peso
        self.bitAtivo = bitAtivo
        self.UsuarioAlteracao = UsuarioAlteracao
        self.DataInserido = DataInserido
        self.IdProdutoNaoUsaMais = IdProdutoNaoUsaMais


class MarcaProduto(db.Model):
    __tablename__ = 'Marca'
    IdMarca = db.Column(db.Integer, primary_key=True, unique=True)
    Marca = db.Column(db.String(), nullable=True, unique=False)
    PrazoFabricacao = db.Column(db.Integer, nullable=True, unique=False)
    PedidoMinimo = db.Column(db.Integer, nullable=True, unique=False)
    Sobre = db.Column(db.String(), nullable=True, unique=False)
    Video = db.Column(db.String(), nullable=True, unique=False)
    DataCadastro = db.Column(DateTime(timezone=True), server_default=func.now())
    DataAtualizacao = db.Column(DateTime(timezone=True), server_default=func.now())
    IncluidoPor = db.Column(db.String(), nullable=True, unique=False)
    AlteradoPor = db.Column(db.String(), nullable=True, unique=False)
    BitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
    IdMarca2 = db.Column(db.Integer, nullable=True, unique=False)
    ImgNome = db.Column(db.String(), nullable=True, unique=False)
    bitShowRoom = db.Column(db.Boolean, nullable=True, unique=False)


    def __init__(self,Marca,PrazoFabricacao,PedidoMinimo,Sobre,Video, 
        DataCadastro,DataAtualizacao, IncluidoPor,AlteradoPor,BitAtivo, IdMarca2, ImgNome, bitShowRoom ):
        self.Marca = Marca
        self.PrazoFabricacao = PrazoFabricacao
        self.PedidoMinimo = PedidoMinimo
        self.Sobre = Sobre
        self.Video = Video
        self.DataCadastro = DataCadastro
        self.DataAtualizacao = DataAtualizacao
        self.IncluidoPor = IncluidoPor
        self.AlteradoPor = AlteradoPor
        self.BitAtivo = BitAtivo
        self.IdMarca2 = IdMarca2
        self.ImgNome = ImgNome
        self.bitShowRoom = bitShowRoom


class SubCategoria(db.Model):
    __tablename__ = 'SubCategoria'
    IdSubCat = db.Column(db.Integer, primary_key=True, unique=True)
    IdCat = db.Column(db.Integer, nullable=True, unique=False)
    NomeSubCat = db.Column(db.String(), nullable=True, unique=False)
    BitAtivo = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,IdCat,NomeSubCat, BitAtivo):
        self.IdCat = IdCat
        self.NomeSubCat = NomeSubCat
        self.BitAtivo = BitAtivo


class Categoria(db.Model):
    __tablename__ = 'Categoria'
    IdCat = db.Column(db.Integer, primary_key=True, unique=True)
    NomeCat = db.Column(db.String(), nullable=True, unique=False)
    IdDept = db.Column(db.Integer, nullable=True, unique=False)
    BitAtivo = db.Column(db.Boolean, nullable=True, unique=False)
 
    def __init__(self,NomeCat,IdDept,BitAtivo):
        self.NomeCat = NomeCat
        self.IdDept = IdDept
        self.BitAtivo = BitAtivo


class Departamento(db.Model):
    __tablename__ = 'Departamento'
    IdDept = db.Column(db.Integer, primary_key=True, unique=True)
    NomeDept = db.Column(db.String(), nullable=True, unique=False)
    BitAtivo = db.Column(db.Boolean, nullable=True, unique=False)

    def __init__(self,NomeDept, BitAtivo):
        self.NomeDept = NomeDept
        self.BitAtivo = BitAtivo


class EspecificacaoProdutoss(db.Model):
    __tablename__ = 'EspecificacaoProdutos'
    IdSpec = db.Column(db.Integer, primary_key=True, unique=True)
    SKU = db.Column(db.String(), nullable=True, unique=False)
    NomeEspecificacao = db.Column(db.String(), nullable=True, unique=False)
    ValorEspecificacao = db.Column(db.String(), nullable=True, unique=False)

    def __init__(self,SKU,NomeEspecificacao, ValorEspecificacao ):
        self.SKU = SKU
        self.NomeEspecificacao = NomeEspecificacao
        self.ValorEspecificacao = ValorEspecificacao
        








        

