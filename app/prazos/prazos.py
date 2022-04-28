from flask import Blueprint, render_template, redirect,url_for



prazos = Blueprint('prazos', __name__)


@prazos.route("/prazos",methods=['GET','POST'])
def indexprazos():
    return 'prazos'