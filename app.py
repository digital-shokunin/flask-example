from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    client = request.headers.get('User-Agent')
    return render_template("index.html",
        title = 'Home',
        client = client)
        
if __name__ == '__main__':
    app.run()
