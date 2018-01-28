from config import app_details
from flask import Blueprint, render_template, request
from functools import wraps


cpk = Blueprint('cpk', __name__,
            static_folder="static/",
            static_url_path="/%s" % __name__,
            template_folder="templates/"
        )


def needs_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        pass
    return wrapper


@cpk.route('/')
def index():
    return render_template('index.html')


@cpk.route('/get_currencies')
def get_currencies():
    # get a list of currencies
    return "Here are a list of currencies!"


@cpk.route('/get_exchange_amount', methods=['POST'])
def get_exchange_amount(curr):
    from_curr = request.form['from_curr']
    to_curr = request.form['to_curr']
    amount = request.form['amount']
    # check if the amount for the current exchange is
    # greater that the min amount for the transfer to work
    return "1.1"


@cpk.route('/create_transcation')
def create_transaction():
    return "Transferring the money"


@cpk.route('/get_status/<tid>')
def get_status(tid):
    return "Getting the status of " + tid
