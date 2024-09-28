from flask import Flask, render_template
from flask_login import login_manager
from routes.admin import admin_route

app = Flask(__name__)

app.register_blueprint(admin_route, url_prefix = '/lista')

@app.route('/')
def index():

    return render_template('index.html')

app.run(debug=True)
login_manager = login_manager()