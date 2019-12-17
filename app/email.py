from flask import render_template
from flask_mail import Message
from app import theapp, mail

def send_email(subject, sender, recipients, text_body, html_body):
	msg = Message(subject, sender=sender, recipients=recipients)
	msg.body = text_body
	msg.html = html_body
	# app context ?
	mail.send(msg)

def send_password_reset_email(user):
	pass # TODO