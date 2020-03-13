from dotenv import load_dotenv
import os


load_dotenv() # On met dans le .env pour cacher les données sensibles...
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	ADMINS = ['charlie.faucher@gmail.com']
	LANGUAGES = ['en', 'fr']
	REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'waf-wouf'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
	POSTS_PER_PAGE = 10
	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')