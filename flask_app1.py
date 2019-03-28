from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="JaykumarPatel480",
    password="MySQLDataBase",
    hostname="JaykumarPatel4802.mysql.pythonanywhere-services.com",
    databasename="JaykumarPatel480$TrackUrTransit",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

comments = []

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("index.html")

@app.route('/search/', methods=['GET'])
def search():
    # found in ../templates/
    return render_template("search_page.html")

@app.route('/map/', methods=['GET'])
def map():
    # found in ../templates/
    return render_template("map.html")
