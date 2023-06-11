from __future__ import annotations

from functools import wraps

from .app import current_app
from .exceptions import NoSessionException

HOST = 'http://localhost'


def gen_proxy_from_port(host: str = None, port: int = None):
    if host is None:
        return None
    if port is None:
        return {
            'http': f'{host}',
            'https': f'{host}'
        }
    return {
        'http': f'{host}:{port}',
        'https': f'{host}:{port}'
    }


def bind_app_config(needs_session: bool = False):
    def decorator(f):
        @wraps(f)
        def wrapper_func(*args, **kwargs):
            host = kwargs.pop('host', None)
            port = kwargs.pop('port', None)
            auth_token = kwargs.pop('auth_token', None)
            if needs_session:
                try:
                    session = current_app().config.session
                    if auth_token is None:
                        auth_token = session['access_token']
                except ValueError:
                    session = None
                if session is None and auth_token is None:
                    raise NoSessionException(
                        'You need to set a session in the config section '
                        'or pass the variable `auth_token` to the function.\n'
                        '>>> from mypass_requests import MyPassRequests\n\n'
                        '>>> app = MyPassRequests()\n'
                        '>>> app.config.session = <your session object>')
            if host is None:
                try:
                    host = current_app().config.host
                except ValueError:
                    host = HOST
            if port is None:
                try:
                    port = current_app().config.port
                except ValueError:
                    pass

            if auth_token is None:
                return f(*args, **kwargs, host=host, port=port)
            return f(*args, **kwargs, host=host, port=port, auth_token=auth_token)

        return wrapper_func

    return decorator


def bind_error_handlers(f):
    @wraps(f)
    def wrapper_func(*args, **kwargs):
        # in case no application is configured, the original wrapped function will be called
        try:
            # get error handlers
            error_handlers = current_app().error_handlers
            # try running the function
            try:
                return f(*args, **kwargs)
            # can we handle any of these errors?
            except tuple(error_handlers.keys()) as e:
                handler = error_handlers[type(e)]
                return handler(f, e, *args, **kwargs)
        except ValueError:
            return f(*args, **kwargs)

    return wrapper_func
