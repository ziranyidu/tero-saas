from modules.bots import telegram 
from flask import (
    Flask,
    render_template
)
import logging


app = Flask(__name__)
app.register_blueprint(telegram, url_prefix='/bots/telegram')


@app.route('/')
def hello():
    return render_template('index.html') 


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500