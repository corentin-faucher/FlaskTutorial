from app import theapp, db, cli
from app.models import User, Post

@theapp.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}
