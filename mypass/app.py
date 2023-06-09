from .types import MyPassConfig


class MyPassRequests:
    _instance: 'MyPassRequests' = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance') or cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._config = MyPassConfig()

    @property
    def config(self):
        return self._config


# noinspection PyProtectedMember
def current_app():
    if not hasattr(MyPassRequests, '_instance') or MyPassRequests._instance is None:
        raise ValueError('App has not been initialized yet.')
    return MyPassRequests._instance
