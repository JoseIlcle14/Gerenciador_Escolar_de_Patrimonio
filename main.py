from flask import Flask, render_template

from routes.admin import admin_route

app = Flask(__name__)

app.register_blueprint(admin_route, url_prefix = '/lista')

@app.route('/')
def index():

    return render_template('index.html')

app.run(debug=True)