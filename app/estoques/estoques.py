from flask import Blueprint, render_template, redirect,url_for



estoques = Blueprint('estoques', __name__,template_folder='templates',static_folder='static',static_url_path='/static/imagens')


@estoques.route("/estoques",methods=['GET','POST'])
def indexestoques():
    
    return 'estoques'