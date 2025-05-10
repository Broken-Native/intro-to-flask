from flask import Blueprint


bp = Blueprint("auth", __name__, url_prefix="/auth")

from . import sign_in, sign_up