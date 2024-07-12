from flask import Flask, request, jsonify, send_from_directory,render_template
import os
from pymongo import MongoClient 
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ashok1234:ashok1234@cluster0.kffhmzo.mongodb.net/'

client = MongoClient(app.config['MONGO_URI'])
db = client['Hotelbooking']

class User:
    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password=password

    def save(self):
        user_dict = self.__dict__
        result = db.users.insert_one(user_dict)
        return result.inserted_id
    

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
   if(request.method=="POST"):
      email=request.form.get('email')
      password=request.form.get('password')
      message=checkForValidationLogin(email,password)

      if(message):
         return render_template('login.html',message=message)
      else:
         user=db.users.find_one({"email":email})
         if(user):
            if(user.password!=password):
               return render_template('login.html',message="Wrong password")
            else:
               return render_template('index.html',message="Login Successfull!")


   return render_template('login.html')


@app.route('/register' ,methods=['GET','POST'])
def register():
   if(request.method=='POST'):
      name=request.form.get('name')
      email=request.form.get('email')
      password=request.form.get('password')
      confirmPassword=request.form.get('confirmpassword')
      print(name,email,password,confirmPassword) 
      message=checkForValidationRegister(name,email,password,confirmPassword)

      if(message):
          return render_template('register.html',message=message)
      else:
          user=db.users.find_one({"email":email})
          if(user):
              return render_template('register.html',message="User already registered!")
          else:
              db.users.insert_one({"name":name,"email":email,"password":password})
              return render_template('register.html',message="User registered successfully!")

   return render_template('register.html',message="")

def checkForValidationLogin(email,password):
   if(email==""):
      return "email is empty"
   elif(password==""):
      return "password is empty"
   
def checkForValidationRegister(name,email,password,confirmPassword):
   if(name==""):
      return "name is empty"
   elif(email==""):
      return "email is empty"
   elif(password==""):
      return "password is empty"
   elif(confirmPassword==""):
      return "confirm password is empty"
   elif(confirmPassword!=password):
      return "password not match"
   
@app.route('/favourites')
def favourites():
   return render_template('favourites.html')

@app.route('/destination')
def destination():
   path=request.args.get('name')
   return render_template('destinationpage.html')


if __name__ == '__main__':
    app.run(debug=True)    


