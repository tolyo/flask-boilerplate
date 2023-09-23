from flask import Flask, render_template
from web.home import home

app = Flask(
    __name__,
    template_folder='',
    static_folder='web'
)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(home.home)

if __name__ == '__main__':
    app.run()