from flask import Flask, request, render_template, send_file
from data import *

app = Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/')
# def hello():
#     return 'Hello, World!'

@app.route('/')
def root():
   return render_template('index.html', markers1=map1, markers2=map2, markers3=map3)

@app.route('/image1')
def image1():
   print(1)
   return send_file('templates/static/image1.png')

@app.route('/image2')
def image2():
   print(1)
   return send_file('templates/static/image2.jpg')

@app.route('/image3')
def image3():
   print(1)
   return send_file('templates/static/image3.png')

@app.route('/label2')
def image4():
   print(1)
   return send_file('templates/static/label2.png')

@app.route('/label3')
def image5():
   print(1)
   return send_file('templates/static/label3.png')


if __name__ == '__main__':
   app.run(host='10.215.15.59')
