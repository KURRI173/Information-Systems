from flask import Flask, request, jsonify, send_from_directory,render_template
import os
from pymongo import MongoClient 
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'

mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database()

# Route for home
@app.route('/')
def home():
   return render_template('index.html')

# Route for login
@app.route('/login')
def login():
   return render_template('login.html')

# Route for login
@app.route('/register')
def register():
   return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)    


