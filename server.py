from flask import Flask, request, jsonify, send_from_directory,render_template,session
import os
from pymongo import MongoClient 
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://ashok1234:ashok1234@cluster0.kffhmzo.mongodb.net/'

client = MongoClient(app.config['MONGO_URI'])
db = client['Hotelbooking']

app.secret_key="123"

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
            if(user['password']!=password):
               return render_template('login.html',message="Wrong password")
            else:
               session['user']=user['email']
               return render_template('index.html',message="logout")

   return render_template('login.html',message="")

@app.route("/search/<ID>")
def search(ID):
    products = product_collection.find({"name": {'$regex': ID, '$options': 'i'}})
    result = []
    for product in products:
        product['_id'] = str(product['_id'])  
        result.append(product)
        print(result)
    return jsonify(result), 200


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
   
@app.route('/favourites',methods=['GET','POST'])
def favourites():
   if(session.get('user')):
         return render_template('favourites.html',message='Logout')
   return render_template('favourites.html',message='')

@app.route('/destination')
def destination():
   if(session.get('user')):
      return render_template('destinationpage.html',message='Logout')
   return render_template('destinationpage.html',message='')

@app.route('/famous')
def famous():
   path=request.args.get('name')
   if(session.get('user')):
         return render_template('famoussearches.html',message='Logout')
   return render_template('famoussearches.html')


@app.route('/logout')
def logout():
   session['user']=''
   return render_template('index.html')


product_collection = db['products']  

@app.route('/addproducts', methods=['POST'])
def add_products():
    ProductCollection = [
        {"name": "Barcelona", "price": "$200", "imgpath": "static/Assets/panel1image1.avif"},
        {"name": "Alomar", "price": "$1200", "imgpath": "static/Assets/panel1image2.avif"},
        {"name": "Valentine Cabillers", "price": "$800", "imgpath": "static/Assets/panel1image3.avif"},
        {"name": "Cork", "price": "$200", "imgpath": "static/Assets/panel2img1.avif"},
        {"name": "Newyork", "price": "$1200", "imgpath": "static/Assets/panel2img2.avif"},
        {"name": "Sand", "price": "$1100", "imgpath": "static/Assets/panel2img3.avif"},
        {"name": "San fransisco", "price": "$1800", "imgpath": "static/Assets/panel2img4.avif"},
    ]
    
    result = product_collection.insert_many(ProductCollection)
    return jsonify({"message": f"Inserted {len(result.inserted_ids)} documents into the products collection."}), 200


if __name__ == '__main__':
    app.run(debug=True)    


