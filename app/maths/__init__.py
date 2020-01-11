from flask import Blueprint

bp = Blueprint('maths', __name__)

from app.maths import routes