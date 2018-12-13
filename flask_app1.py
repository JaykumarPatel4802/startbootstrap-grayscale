from flask import Flask, request, render_template
app = Flask(__name__)
app.static_folder = 'static'

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