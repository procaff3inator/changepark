import copy
import hashlib
import hmac
import json
import requests
from functools import wraps

def api_method(f):
    """Decorate functions that are API methods.

    :param f: A function/method to be wrapped
    """
    @wraps(f)
    def d(*args, **kwargs):
        payload = f(*args, **kwargs)
        print(payload)
        return requests.post(
                    payload['url'],
                    headers=payload['headers'],
                    data=payload['payload']
                )
    return d


class Changelly(object):

    def __init__(self, url, key, secret):
        self.url = url
        self.key = key
        self.secret = secret

    def _prepare_payload(self, params):
        json_pl = {'jsonrpc': '2.0', 'id': 1 }
        json_pl.update(params)
        serialized_data = json.dumps(json_pl)
        sign = hmac.new(
                    self.secret.encode('utf-8'),
                    serialized_data.encode('utf-8'),
                    hashlib.sha512
                ).hexdigest()
        headers = {
            'api-key': self.key,
            'sign': sign,
            'Content-type': 'application/json',
        }

        return {'url': self.url, 'payload': serialized_data, 'headers': headers}

    @api_method
    def get_currencies(self):
        """Fetch a list of supported currencies from the server."""
        params = {
            'method': 'getCurrencies',
            'params': [],
        }
        return self._prepare_payload(params)

    @api_method
    def get_min_amount(self, fromcurr, tocurr):
        """Get min amount that can be exchanged between
        two different currencies.

        :param fromcurr: Currency to change from
        :param tocurr: Currency to change to
        """
        return self._prepare_payload({
                        'method': 'getMinAmount',
                        'params': {
                            'from': fromcurr,
                            'to': tocurr,
                        },
                        'id': 1,
                    })

    @api_method
    def get_exchange_amount(self, fromcurr, tocurr, amount):
        """Get the exchange amount between two different
        currencies.
        :param fromcurr: Currency to change from
        :param tocurr: Currency to change to
        :param amount: Amount to be exchaned
        """
        return self._prepare_payload({
                        'method': 'getExchangeAmount',
                        'params': {
                            'from': fromcurr,
                            'to': tocurr,
                            'amount': amount,
                        },
                        'id': 1,
                    })

    @api_method
    def get_status(self, transaction_id):
        """Get the status of a transaction.

        :param transaction_id: Id of the transaction
        """
        return self._prepare_payload({
                        "method": "getStatus",
                        "params": {
                            "id": transaction_id
                         },
                         "id": 1
                    })

    @api_method
    def create_transaction(self, fromcurr, tocurr, amount, **kwargs):
        """Create a transation to convert from one currency to another.

        :param fromcurr: From Currency
        :param tocurrency: To Currency
        :param amount: Amount to send
        :param extra_id: required for XRP, STEEM/SBD, XLM, DCT, XEM
        :param refund_address: optional param, enables refund
        :param refund_extraid: required for XRP, STEEM/SBD, XLM, DCT, XEM
        """
        raise NotImplementedError("WIP")
        params = {
            'from': fromcurr,
            'to': tocurr,
            'amount': amount,
        }

        if kwargs:
            params.update(kwargs)

        return self._prepare_payload({
                        'method': 'createTransaction',
                        # 'params': ,
                        'id': 1,
                    })

    @api_method
    def get_transactions(self, **kwargs):
        """Get a list of transactions according to the filter
        params passed.

        :param currency: Currency to filter from
        :param address:  Address to filter by
        :param extraId:  Extra id needed by some currencies
        :param limit:    Result limit
        :param offset:   Result offset
        """
        return self._prepare_payload({
                        'method': 'getTransactions',
                        'params': {},
                        'id': 1,
                    })


if __name__ == '__main__':
    from config import api_creds
    c = Changelly(
            api_creds['url'],
            api_creds['key'],
            api_creds['secret']
        )
    # print("Foo: {}".format(c.get_currencies().text))
    # print("Foo: {}".format(c.get_exchange_amount("btc", "eth", "100").text))
    # print("Foo: {}".format(c.create_transaction("btc", "eth", "100")))
    # print("Foo: {}".format(c.get_status('f6e0c6a5bb05').text))
    print("Foo: {}".format(c.get_status('4bb51c2cca9b').text))
    # print("Foo: {}".format(c.get_transactions().text))
