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
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

db.Comments

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


if __name__ == '__main__':
    app.run()

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    # found in ../templates/
    return render_template("search_page.html")

@app.route('/create_email', methods=["GET", "POST"])
def create_email(request):
    # SQL to update database with STATIC info
    # db.Comments.update("static_email_for_now@gmail.com")

    #comment = Comment(content="test_email@gmail.com")
    # db.session.add(comment)
    # db.session.commit()
    #
    #
    # found in ../templates/
    if request.method == "GET":
        return render_template("index.html", comments=Comment.query.all())

    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/map/', methods=['GET'])
def map():
    # found in ../templates/
    return render_template("map.html")


# https://blog.pythonanywhere.com/121/