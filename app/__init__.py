from flask import Flask
from .index.index import index
from .api.api_routes import api_routes
from .precos.precos import precos
from .prazos.prazos import prazos
from .estoques.estoques import estoques
from .produtos.produtos import produtos
from .models.estoques import MovimentacaoEstoque,LogMovimentacaoEstoque,Estoque
from .models.prazos import ProdutoPrazo, ProdutoPrazoProducFornec, PrazosTransporte
from .models.precos import ProdutoPreco, ProdutoPrecoFrete, ProdutoPrecoBase
from .models.produtos import ProdutoBasico, ProdutoDetalhe, MarcaProduto
from .models.sellers import ProdutoPrecoGoogle, InformacaoSeller, GoogleMenorPreco
from urllib.parse import quote_plus
import pyodbc
from .extensions import db,admin, mail
import os

parametros = (
"Driver={SQL Server Native Client 11.0};"
"Server=w2019.hausz.com.br;"
"Database=HauszMapa;"
"UID=Aplicacao;"
"PWD=S3nh4Apl!caca0"

)

def create_app():
    
    app = Flask(__name__,static_folder=None)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    url_db = quote_plus(parametros)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    mail.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
 

    with app.app_context():
        app.register_blueprint(index)
        app.register_blueprint(produtos)
        app.register_blueprint(precos)
        app.register_blueprint(prazos)
        app.register_blueprint(estoques)
        app.register_blueprint(api_routes)

    return app


