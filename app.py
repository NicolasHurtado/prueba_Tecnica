
from flask import Flask,jsonify,request,render_template,redirect,url_for,session
from db import Session , engine,connection_db

app = Flask(__name__)

app.config['SECRET_KEY']='Th1s1ss3cr3t'

#BD 
app.config['SQLALCHEMY_DATABASE_URI'] = connection_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")