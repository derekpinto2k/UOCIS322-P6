from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/ListAll')
def listeverything():
    dtype = request.args.get('dtype')
    top = request.args.get('top')
    app.logger.debug(top)
    r = requests.get('http://restapi:5000/ListAll/'+dtype, params={'top': top})
    return r.text

@app.route('/ListOpenOnly')
def listopen():
    dtype = request.args.get('dtype')
    r = requests.get('http://restapi:5000/ListOpenOnly/'+dtype)
    return r.text

@app.route('/ListCloseOnly')
def listclose():
    dtype = request.args.get('dtype')
    r = requests.get('http://restapi:5000/ListCloseOnly/'+dtype)
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
