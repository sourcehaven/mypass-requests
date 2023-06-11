from __future__ import annotations

from typing import Any, Callable

from .types import MyPassConfig


class MyPassRequests:
    """
    Application configuration interface. It helps you with adding a global application configuration.

    Note:
        Not process or thread safe, configuration should be done in the main process, and nowhere else.
    """

    _instance: 'MyPassRequests' = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # stores application configuration
        self._config = MyPassConfig()
        # stores error handlers per Exception type
        # error handlers should accept at least two arguments,
        # the original function to be handled, and the exception thrown
        self._error_handlers: dict[
            type[Exception], Callable[[callable, Exception, tuple[Any], dict[str, Any]], Any]] = dict()

    @property
    def config(self):
        return self._config

    @property
    def error_handlers(self):
        return self._error_handlers

    def register_error_handler(
            self,
            exception: type[Exception],
            f: Callable[[callable, Exception, tuple[Any], dict[str, Any]], Any]
    ):
        self._error_handlers[exception] = f


# noinspection PyProtectedMember
def current_app():
    """
    Fetches the current application configuration instance.

    :returns: Application instance
    :raises ValueError: Raises value error, if you are trying to use the instance without creating one first.
    """
    if not hasattr(MyPassRequests, '_instance') or MyPassRequests._instance is None:
        raise ValueError('App has not been initialized yet.')
    return MyPassRequests._instance
