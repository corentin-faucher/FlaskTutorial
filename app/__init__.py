from config import Config
from elasticsearch import Elasticsearch
from flask import Flask, request, current_app
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os



babel = Babel()
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
moment = Moment()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')



def create_app(config_class=Config):
	theapp = Flask(__name__)
	theapp.config.from_object(config_class)

	db.init_app(theapp)
	migrate.init_app(theapp, db)
	login.init_app(theapp)
	mail.init_app(theapp)
	bootstrap.init_app(theapp)
	moment.init_app(theapp)
	babel.init_app(theapp)

	theapp.elasticsearch = Elasticsearch([theapp.config['ELASTICSEARCH_URL']]) \
		if theapp.config['ELASTICSEARCH_URL'] else None

	from app.errors import bp as errors_bp
	theapp.register_blueprint(errors_bp)

	from app.auth import bp as auth_bp
	theapp.register_blueprint(auth_bp, url_prefix='/auth')

	from app.main import bp as main_bp
	theapp.register_blueprint(main_bp)

	if not theapp.debug and not theapp.testing:
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
		if theapp.config['LOG_TO_STDOUT']:
			stream_handler = logging.StreamHandler()
			stream_handler.setLevel(logging.INFO)
			theapp.logger.addHandler(stream_handler)
		else:
			if not os.path.exists('logs'):
				os.mkdir('logs')
			file_handler = RotatingFileHandler('logs/coqblog.log', maxBytes=10240, backupCount=10)
			file_handler.setFormatter(logging.Formatter(
				'%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'))
			file_handler.setLevel(logging.INFO)
			theapp.logger.addHandler(file_handler)
		
		theapp.logger.setLevel(logging.INFO)
		theapp.logger.info('Coqblog startup')

	return theapp


@babel.localeselector
def get_locale():
	return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
