from flask import Flask
from config import *

from lott.api import api
from lott.api.models import *

app = Flask(__name__)

app.register_blueprint(api)

app.config.from_object(config['develop'])

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
