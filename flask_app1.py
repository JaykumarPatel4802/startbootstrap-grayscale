from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config["DEBUG"] = True

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

@app.route('/login/', methods=['GET'])
def login():
    # found in ../templates/
    return render_template("login.html")

# @app.route('/subscribe', methods=['POST'])
# def subscribe():
#     # found in ../templates/
#     email = request.form['inputEmail']
#     with open('./subscribe.csv') as f:
#         f.write(email + "\n")
#     return render_template("login.html")

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{JaykumarPatel4802}:{MySQLDataBase}@{JaykumarPatel4802.mysql.pythonanywhere-services.com}/{TrackUrTransit}".format(
    username="JaykumarPatel480",
    password="MySQLDataBase",
    hostname="JaykumarPatel4802.mysql.pythonanywhere-services.com",
    databasename="TrackUrTransit",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
