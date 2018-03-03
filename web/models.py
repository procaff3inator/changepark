import hashlib
from config import database as dbconfig
from orator import DatabaseManager, Model, scope

db = DatabaseManager(dbconfig)
Model.set_connection_resolver(db)

class User(Model):

    __table__ = 'cp_users'

    __fillable__ = [
        'username',
        'password',
        'enabled',
    ]

    @classmethod
    def create(cls, **kwargs):
        """Create a new user.

        :param username: Name of the new user
        :param password: New password for the user
        :param enabled:  If the user is active or inactive
        """
        kwargs['enabled'] = 1
        return super(User, cls).create(**kwargs)

class History(Model):
    
    __table__ = 'cp_history'

    __fillable__ = [
        'user_id',
        'from_curr',
        'to_curr',
        'amount',
        'address_in',
        'address_out',
        'extraid',
        # 'refund_address',
        # 'refund_extraid',
        'transaction_id',
        'exchange_status',
    ]

    @scope
    def get_pending(self, query):
        return self.query.where('sync', '0')
