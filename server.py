from flask import Flask, request, jsonify, send_from_directory,render_template
import os
from pymongo import MongoClient 
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ashok1234:ashok1234@cluster0.kffhmzo.mongodb.net/'

client = MongoClient(app.config['MONGO_URI'])
db = client['Hotelbooking']

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
   return render_template('login.html')


@app.route('/register' ,methods=['GET','POST'])
def register():
   if(request.method=='POST'):
      name=request.args.get('name')
      email=request.args.get('email')
      password=request.args.get('password')
      confirmPassword=request.args.get('confirmPassword')

      print(name,email,password,confirmPassword)   
   return render_template('register.html')


@app.route('/favourites')
def favourites():
   return render_template('favourites.html')

@app.route('/destination')
def destination():
   path=request.args.get('name')
   return render_template('destinationpage.html')


if __name__ == '__main__':
    app.run(debug=True)    


