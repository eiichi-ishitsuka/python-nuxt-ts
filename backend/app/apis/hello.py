from flask import Blueprint, jsonify

from app.models import hello

api = Blueprint('hello',
                __name__,
                url_prefix='/api')


@api.route('hello')
def get():
    print("aaa")
    data = hello.execute()
    return jsonify(data), 200
