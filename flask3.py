from app import create_app, db, cli
from app.models import Message, Notification, Post, Task, User

theapp = create_app()
cli.register(theapp)


@theapp.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
		'Notification': Notification, 'Task': Task}
