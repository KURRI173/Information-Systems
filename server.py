from flask import Flask, request, jsonify, send_from_directory,render_template
import os
from pymongo import MongoClient 
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'

mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database()


@app.route('/')
def home():
   return render_template('index.html')


@app.route('/login')
def login():
   return render_template('login.html')


@app.route('/register')
def register():
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


