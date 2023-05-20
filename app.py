from flask import Flask, url_for
from apps import register_blueprints


app = Flask(__name__)
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)