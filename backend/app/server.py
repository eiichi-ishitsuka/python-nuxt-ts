from flask import Flask

from app.apis import hello

app = Flask(__name__)
app.register_blueprint(hello.api)