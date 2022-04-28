from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_mail import Mail, Message

db = SQLAlchemy()
admin = Admin(name='Admin', template_mode='bootstrap4')


mail = Mail()