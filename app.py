from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# 404 page
@app.errorhandler(404)
def error(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=80, debug=True)