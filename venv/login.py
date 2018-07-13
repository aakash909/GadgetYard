from flask import *
app = Flask(__name__)

@app.route('/')
def Login():
   return render_template('Login.html')
   #return render_template('firstpage.html')

@app.route('/login/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      email = request.form['email']
      passw = request.form['pass']
      print(email," ",passw)
      return render_template('demo.html')

if __name__ == '__main__':
   app.run(debug = True)

