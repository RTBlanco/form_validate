from flask import Flask

app = Flask(__name__)

from form_validate import routes
