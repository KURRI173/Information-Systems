from flask import Flask, request, jsonify, send_from_directory,render_template
import os

app = Flask(__name__)


# Route for home
@app.route('/')
def home():
   return render_template('index.ejs')

if __name__ == '__main__':
    app.run(debug=True)    


