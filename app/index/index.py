from flask import Blueprint, render_template, redirect,url_for
from ..controllers.helpers import filtrar_subcategorias,filtrar_categorias,filtrar_departamentos,filtrar_marcas
from ..controllers.helpers_dashboard import selectiona_unidade,seleciona_periodos_pedido_loja,filtra_vendas_dia_loja,venda_loja,selecionamarca_mesatual,filtrospedidos
from ..models.forms import Selectfiledform

index = Blueprint('index', __name__,template_folder='templates',static_folder='static',static_url_path='/static/imagens')


@index.route("/",methods=['GET'])
def home():
    
    return render_template('index.html')


@index.route("/dashboard",methods=['GET'])
def dashboard():
    marcas = filtrar_marcas()
    departamentos = filtrar_departamentos()
    unidades = selectiona_unidade()
    datapedidos = seleciona_periodos_pedido_loja()
    datadiario = filtra_vendas_dia_loja()
    vendasmes = venda_loja()


    return render_template('dashboard.html',marcas=marcas,departamentos=departamentos
    ,unidades=unidades,datapedidos=datapedidos,datadiario=datadiario,vendasmes=vendasmes)


@index.route("/marca/<refmarca>",methods=['GET'])
def marcavenda(refmarca):
    produtos = selecionamarca_mesatual(refmarca)
    filtrosmarca = filtrospedidos(refmarca)

    return render_template('marcaunitaria.html',produtos=produtos,filtrosmarca=filtrosmarca)

@index.route("/pedidos/<ref>",methods=['GET'])
def pedidodetalhes(ref):
    return 'Olaaa'


@index.route("/pedidoun/<refid>",methods=['GET'])
def pedidounitario():
    return "pedido"