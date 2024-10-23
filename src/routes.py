from .modules.auth.auth_module import auth_module
from .modules.user.user_module import user_module


def register_routes(app):
    user_module(app)
    auth_module(app)
