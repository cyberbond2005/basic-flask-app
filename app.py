#from flask import Flask, render_template
#app = Flask(__name__)

# two decorators, same function
#@app.route('/')
#@app.route('/index.html')
#def index():
#    return render_template('index.html', the_title='Tiger Home Page')

#@app.route('/symbol.html')
#def symbol():
#    return render_template('symbol.html', the_title='Tiger As Symbol')

#@app.route('/myth.html')
#def myth():
#    return render_template('myth.html', the_title='Tiger in Myth and Legend')
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
