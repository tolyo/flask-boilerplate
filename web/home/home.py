from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/_home')
def my_route():
   return render_template('web/home/home.html')
