from flask import Flask, render_template

app = Flask(
    __name__, 
    template_folder='app',
    static_folder='app'
)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user/user.html')

if __name__ == '__main__':
    app.run()