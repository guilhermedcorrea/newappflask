from flask import Blueprint, render_template, redirect,url_for



precos = Blueprint('precos', __name__)


@precos.route("/precos",methods=['GET','POST'])
def indexprecos():
    return 'precos'