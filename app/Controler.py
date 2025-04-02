#Controler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# creating 
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
