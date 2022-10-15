from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
app = Flask(__name__)

@app.route('/')
def wandrea():
    return "hello world"


if __name__ == "__main__":
    app.run()


#run by typing     python app.py     in terminal, but first change cd to backend 