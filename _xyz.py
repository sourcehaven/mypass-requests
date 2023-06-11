import logging
from pathlib import Path

import requests

from mypass import MyPassRequests, crypto, db
from mypass.exceptions import MyPassRequestException


def mypass_request_exception_handler(f, e, *args, **kwargs):
    response = requests.post('http://localhost:5757/api/auth/login', json={'pw': 'my-super-secret'})
    app.config.session = response.json()
    print('Logging in again ...')
    kwargs.pop('auth_token', None)
    return f(*args, **kwargs)


if __name__ == '__main__':
    app = MyPassRequests()
    app.config.host = 'http://localhost'
    app.config.port = 5757
    app.register_error_handler(MyPassRequestException, mypass_request_exception_handler)

    resp = requests.post('http://localhost:5757/api/auth/login', json={'pw': 'my-super-secret'})
    if resp.status_code == 201:
        access_token = resp.json()['access_token']
        refresh_token = resp.json()['refresh_token']
        app.config.session = resp.json()
        try:
            created_id = db.create_master_pw(pw='my-super-secret')
            print('Created Id   :', created_id)
            pw_stored = db.query_master_pw()
            print('Stored Pw    :', pw_stored)
            updated_id = db.update_master_pw(pw='my-super-secret-v2')
            print('Updated Id   :', updated_id)
        finally:
            import shutil

            shutil.rmtree(Path.home().joinpath('.mypass', 'db'), ignore_errors=True)

    secret_token, generated_salt = crypto.encrypt('my-secret', 'my-password')
    secret_message = crypto.decrypt(secret_token, 'my-password', generated_salt)
    assert secret_message == 'my-secret'
