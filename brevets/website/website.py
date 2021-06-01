from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/listAll')
def listall():
    dtype = request.args.get('dtype')
    top = request.args.get('top')
    app.logger.debug(top)
    r = requests.get('http://restapi:5000/listAll/'+dtype, params={'top': top})
    return r.text

@app.route('/listOpenOnly')
def listopen():
    dtype = request.args.get('dtype')
    top = request.args.get('top')
    r = requests.get('http://restapi:5000/listOpenOnly/'+dtype, params={'top': top})
    return r.text

@app.route('/listCloseOnly')
def listclose():
    dtype = request.args.get('dtype')
    top = request.args.get('top')
    r = requests.get('http://restapi:5000/listCloseOnly/'+dtype, params={'top': top})
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
