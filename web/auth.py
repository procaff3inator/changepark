import hashlib
from functools import wraps
from .models import User

def get_user_by_id(userid):
    """Get user by id.

    :param userid: Just an integer
    """
    return User.find(userid)

def pw_hasher(plaintextpw, salt):
    """Get the hash of the plain text password.

    :param plaintextpw: Plain text password
    """
    saltmkr = hashlib.sha256()
    s = salt + plaintextpw + salt
    saltmkr.update(s.encode())
    return saltmkr.hexdigest()

def create_user(username, password, salt):
    """Create a new user.

    :param username: New username
    :param password: New password
    :param salt:     Salt to hash the password with
    """
    hashed_password = pw_hasher(password, salt)
    return User.create(username=username, password=hashed_password)

def authenticate_user(username, password, salt):
    """Authenticate a user using their username and
    plain text password.

    :param username: Username
    :param password: Plaintext password
    """
    hashedpw = pw_hasher(password, salt)
    return User.where({
        'username': username,
        'password': hashedpw}).get()
