from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

theapp = Flask(__name__)
theapp.config.from_object(Config)
bootstrap = Bootstrap(theapp)
db = SQLAlchemy(theapp)
migrate = Migrate(theapp, db)
moment = Moment(theapp)
login = LoginManager(theapp)
login.login_view = 'login'
mail = Mail(theapp)

from app import routes, models, errors # akward, mais routes doit importer flaskapp...

if not theapp.debug:
	if theapp.config['MAIL_SERVER']:
		auth = None
		if theapp.config['MAIL_USERNAME'] or theapp.config['MAIL_PASSWORD']:
			auth = (theapp.config['MAIL_USERNAME'], theapp.config['MAIL_PASSWORD'])
		secure = None
		if theapp.config['MAIL_USE_TLS']:
			secure = ()
		mail_handler = SMTPHandler(
			mailhost=(theapp.config['MAIL_SERVER'], theapp.config['MAIL_PORT']),
			fromaddr='no-reply@' + theapp.config['MAIL_SERVER'],
			toaddrs=theapp.config['ADMINS'], subject='Microblog Failure',
			credentials=auth, secure=secure)
		mail_handler.setLevel(logging.ERROR)
		theapp.logger.addHandler(mail_handler)

	if not os.path.exists('logs'):
		os.mkdir('logs')
	file_handler = RotatingFileHandler('logs/coqblog.log', maxBytes=10240, backupCount=10)
	file_handler.setFormatter(logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
	file_handler.setLevel(logging.INFO)
	theapp.logger.addHandler(file_handler)
	theapp.logger.setLevel(logging.INFO)
	theapp.logger.info('Coqblog startup')


