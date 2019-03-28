[1mdiff --git a/__pycache__/flask_app1.cpython-37.pyc b/__pycache__/flask_app1.cpython-37.pyc[m
[1mindex bd0338c..3322c89 100644[m
Binary files a/__pycache__/flask_app1.cpython-37.pyc and b/__pycache__/flask_app1.cpython-37.pyc differ
[1mdiff --git a/flask_app1.py b/flask_app1.py[m
[1mindex 32c6f3e..1a2fa83 100644[m
[1m--- a/flask_app1.py[m
[1m+++ b/flask_app1.py[m
[36m@@ -5,6 +5,27 @@[m [mapp = Flask(__name__)[m
 app.static_folder = 'static'[m
 app.config["DEBUG"] = True[m
 [m
[32m+[m[32mSQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format([m
[32m+[m[32m    username="JaykumarPatel480",[m
[32m+[m[32m    password="MySQLDataBase",[m
[32m+[m[32m    hostname="JaykumarPatel4802.mysql.pythonanywhere-services.com",[m
[32m+[m[32m    databasename="JaykumarPatel480$TrackUrTransit",[m
[32m+[m[32m)[m
[32m+[m[32mapp.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI[m
[32m+[m[32mapp.config["SQLALCHEMY_POOL_RECYCLE"] = 299[m
[32m+[m[32mapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False[m
[32m+[m
[32m+[m[32mdb = SQLAlchemy(app)[m
[32m+[m
[32m+[m[32mclass Comment(db.Model):[m
[32m+[m
[32m+[m[32m    __tablename__ = "comments"[m
[32m+[m
[32m+[m[32m    id = db.Column(db.Integer, primary_key=True)[m
[32m+[m[32m    content = db.Column(db.String(4096))[m
[32m+[m
[32m+[m[32mcomments = [][m
[32m+[m
 @app.route('/', methods=['GET'])[m
 def main():[m
     # found in ../templates/[m
[36m@@ -19,28 +40,3 @@[m [mdef search():[m
 def map():[m
     # found in ../templates/[m
     return render_template("map.html")[m
[31m-[m
[31m-@app.route('/login/', methods=['GET'])[m
[31m-def login():[m
[31m-    # found in ../templates/[m
[31m-    return render_template("login.html")[m
[31m-[m
[31m-# @app.route('/subscribe', methods=['POST'])[m
[31m-# def subscribe():[m
[31m-#     # found in ../templates/[m
[31m-#     email = request.form['inputEmail'][m
[31m-#     with open('./subscribe.csv') as f:[m
[31m-#         f.write(email + "\n")[m
[31m-#     return render_template("login.html")[m
[31m-[m
[31m-SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{JaykumarPatel4802}:{MySQLDataBase}@{JaykumarPatel4802.mysql.pythonanywhere-services.com}/{TrackUrTransit}".format([m
[31m-    username="JaykumarPatel480",[m
[31m-    password="MySQLDataBase",[m
[31m-    hostname="JaykumarPatel4802.mysql.pythonanywhere-services.com",[m
[31m-    databasename="TrackUrTransit",[m
[31m-)[m
[31m-app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI[m
[31m-app.config["SQLALCHEMY_POOL_RECYCLE"] = 299[m
[31m-app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False[m
[31m-[m
[31m-db = SQLAlchemy(app)[m
