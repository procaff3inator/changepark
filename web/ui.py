import json
from config import app_details, api_creds
from flask import Flask, current_app, make_response
from flask import Response, request, render_template
from functools import wraps
from web import activity, auth
from web.changelly import Changelly

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO


cpk = Flask(__name__)


# def needs_auth(f):
    # @wraps(f)
    # def wrapper(*args, **kwargs):
        # if auth.authenticate_user(


@cpk.route('/')
def index():
    responses = '{"result": ["btc","eth","xem","lsk","xmr","game","zec","nlg","strat","rep","ltc","bcn","xrp","doge","nxt","dash","nav","pot","gnt","waves","edg","gup","sys","str","bat","snt","cvc","eos","bch","omg","mco","1st","adx","zrx","btg","dgb"], "jsonrpc": "2.0", "id": 1}'
    currencies = json.loads(responses)["result"]
    current_app.logger.info(currencies)
    return render_template('index.html', currencies=currencies)


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
    user_id = 1
    data = activity.show_history(user_id)
    return render_template('history.html', history=data)


@cpk.route('/export')
def export():
    user_id = 1

    f = StringIO()
    activity.make_csv(user_id, f)
    output = make_response(f.getvalue())

    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"

    return output


@cpk.route('/payment')
def payment():
    return render_template('payments-page.html')


@cpk.route('/get_exchange_amount')
def get_exchange_amount():
    from_curr = request.args['from_curr']
    to_curr = request.args['to_curr']
    amount = request.args['amount']

    # check if the amount for the current exchange is
    # greater that the min amount for the transfer to work
    c = Changelly(
            api_creds['url'],
            api_creds['key'],
            api_creds['secret']
        )
    cresponse = c.get_exchange_amount(from_curr, to_curr, amount)
    current_app.logger.info(cresponse.text)
    return cresponse.text


@cpk.route('/create_transcation')
def create_transaction():
    # validate the transaction

    # make the transaction by calling cl's API
    data = json.loads('{"jsonrpc":"2.0","id":"e19e69b1-a701-4ecc-ae68-00f25b63e16c","result":{"id":"e7ff08db497a","apiExtraFee":"0","changellyFee":"0.5","payinExtraId":null,"status":"new","currencyFrom":"btc","currencyTo":"ltc","amountTo":0,"payinAddress":"3HFoKuvtgG3vhVWfFGsRH7KVnFyhK3dzNi","payoutAddress":"LhNXzB2AWQ1Q2ArLPwefvrwY9cCENtDz47","createdAt":"2018-02-17T13:32:17.000Z"}}')

    # add the user's id to the transaction data
    data['result']['user_id'] = 1

    current_app.logger.info("API response: {}".format(data))

    # insert the entry into our database
    activity.save_transaction(**data['result'])
    return "Transferring the money"
