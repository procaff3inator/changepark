from web import auth
from config import app_details
from flask import Flask, render_template, request
from functools import wraps


cpk = Flask(__name__)


# def needs_auth(f):
    # @wraps(f)
    # def wrapper(*args, **kwargs):
        # if auth.authenticate_user(


@cpk.route('/')
def index():
    return render_template('index.html')


@cpk.route('/login')
def login():
    return render_template('login_page.html')


@cpk.route('/register')
def create_user_from():
    return render_template('register_user')


@cpk.route('/create_user', methods=['POST'])
def create_user():
    # basic form validation
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return 'Please make sure to enter all required fields'
    nuser = auth.create_user(username, password, app_details['password_hash'])

    return nuser.id


@cpk.route('/authenticate', methods=['POST'])
def authenticate():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return 'Please make sure to enter all required fields'

    user = auth.authenticate_user(username, password,
                app_details['password_hash'])
    if user:
        msg = 'Welcome user'
    else:
        msg = 'Invalid credentials'

    return msg


@cpk.route('/history')
def history():
    return render_template('history.html')


@cpk.route('/processing')
def processing_route():
    return render_template('processing.html')


@cpk.route('/get_currencies')
def get_currencies():
    # get a list of currencies
    return '["btc","eth","xem","lsk","xmr","game","zec","nlg","strat","rep","ltc","bcn","xrp","doge","nxt","dash","nav","pot","gnt","waves","edg","gup","sys","str","bat","snt","cvc","eos","bch","omg","mco","1st","adx","zrx","btg","dgb"]'


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
