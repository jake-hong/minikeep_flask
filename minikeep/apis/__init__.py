from flask import Blueprint
from flask_restx import Api
from .user import ns as UserNamespace

blueprint =Blueprint(
    'api',
    __name__,
    url_prefix ='/api'
)

api = Api(
    blueprint,
    title='minikeep',
    wersion='1.0',
    doc ='/docs',
    description='Welcom my api docs'
)

api.add_namespace(UserNamespace)