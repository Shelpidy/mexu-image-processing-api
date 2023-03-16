from flask import Blueprint

router = Blueprint('main',__name__)

@router.route('/')
def index():
    return "Hello Router"