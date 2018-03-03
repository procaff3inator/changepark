import csv
from .models import History


def save_transaction(**kwargs):
    """Save the details of a transaction to the database.

    :param user_id: Id of the user who made the transaction
    """
    if not 'user_id' in kwargs:
        raise AttributeError("Cannot create a transaction without user_id")


    return History.create(
                user_id=kwargs['user_id'],
                from_curr=kwargs['currencyFrom'],
                to_curr=kwargs['currencyTo'],
                amount=kwargs['amountTo'],
                address_in=kwargs['payinAddress'],
                address_out=kwargs['payoutAddress'],
                extraid=kwargs['payinExtraId'],
                transaction_id=kwargs['id'],
                exchange_status=kwargs['status'],
            )


def show_history(user_id):
    """Get the transaction details of a particular user.

    :param user_id: Id of the user whose details to fetch
    """
    return History.where('user_id', user_id).get()


def make_csv(user_id, fobj):
    """Create a csv for a user.

    :param user_id: Id of the user whose details to fetch
    :param fobj: A file object
    """
    data = show_history(user_id)
    report = csv.writer(fobj)
    report.writerow([
        'Status',
        'Date',
        'Amount',
        'From Curr',
        'To Curr',
        'To Address',
    ])
    for row in data:
        report.writerow([
            row.exchange_status.capitalize(),
            row.created_at.strftime('%Y-%m-%d %H:%I:%M'),
            row.amount,
            row.from_curr,
            row.to_curr,
            row.address_out
        ])


def get_pending_transactions():
    """Fetch all pending transactions from the database."""

    return History.get_pending().get()
