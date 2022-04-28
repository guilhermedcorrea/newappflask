from flask import Blueprint, render_template, redirect,url_for
from ..extensions import mail,Message


emails = Blueprint('emails', __name__)

emails.route('/sendmail')
def sendmail():
    msg = Message(subject='testetesteteste', sender='naoresponder@hausz.com.br',
     recipients='guilherme.d.correa@live.com',
     body='emailenviado')

    mail.send(msg)
    return 'emailenviado'