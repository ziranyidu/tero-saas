from flask import (
    Blueprint,
    render_template
)

telegram = Blueprint('telegram', __name__)


@telegram.route('/')
def home():
    return 'blueprint de telegram funcando' 