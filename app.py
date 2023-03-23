from flask import Flask,flash,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///healthcard.db"
app.config['SECRET_KEY'] = "my secret key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Create DB Model
class customer(db.Model):
    firstname = db.Column(db.String(200),nullable=False)
    lastname = db.Column(db.String(200),nullable=False)
    username = db.Column(db.String(200),nullable=False,primary_key=True)
    password =  db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    mobno =  db.Column(db.String(200),nullable=False)
    address = db.Column(db.String(200),nullable=False)
    emergencyContact = db.Column(db.String(200),nullable=False)
    emergencyName = db.Column(db.String(200), nullable=False)
    medicalHistory = db.Column(db.String(200),nullable=False)
    age = db.Column(db.String(200),nullable=False)
    gender = db.Column(db.String(200),nullable=False)
    aadharNo = db.Column(db.String(200),nullable=False)
    bloodGroup = db.Column(db.String(200), nullable=False)
    policyNumber = db.Column(db.String(200), nullable=False)
    familyDoctorName = db.Column(db.String(200), nullable=False)
    familyDoctorContact = db.Column(db.String(200), nullable=False)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_name',None) is None:
            return redirect('/login.php')
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login.php",methods=['GET','POST'])
def logincust():
    if request.method=="POST":
        if (not request.form['username'] or not request.form['password']):
            flash("Please fill all the fields", "error")
        else:
            req_username = request.form['username']
            req_password = request.form['password']
            creds_usr = customer.query.filter_by(username=req_username).all()
            creds_pwd = customer.query.filter_by(password=req_password).all()
            if (creds_usr and creds_pwd):
                session['username'] = req_username
                flash(session['username'])
                return render_template("writenfc.php",curr_usr=req_username)
            else:
                flash('Invalid Credentials! Check your password or Register','error')
                return redirect("login.php")
    else:
        return render_template("login.php")

@app.route("/", methods=['GET','POST'])
def home():
    #db.drop_all()
    #db.create_all()
    #new_customer = customer(firstname = "Beleswar", lastname = "Padhi", username = "20BRS1017", password = "health@123", email = "beleswarprasad@gmail.com", mobno = "6371332737", address = "chennai", emergencyContact = "6372600260", emergencyName = "Jay Kumar Sahoo", medicalHistory = "Prone to dust allergy", age = "21", gender = "male", aadharNo = "78937278043100", bloodGroup = "O+ve", policyNumber = "LIC73829", familyDoctorName = "Dr. Dipanshu Rout", familyDoctorContact = "8790912342")
    #try:
    #    db.session.add(new_customer)
    #    db.session.commit()
    #    return "successfully added beleswar"
    #except:
    #    return "There was error adding a new customer"
    return "Welcome to NFC Reader/Writer"

@app.route("/writenfc.php", methods=['GET','POST'])
#@login_required
def write():
    if request.method=="GET":
        return render_template("writenfc.php")
    elif request.method=="POST":
        try:
            update_customer = customer.query.get_or_404("20BRS1017")
            update_customer.firstname = request.form['firstname']
            update_customer.lastname = request.form['lastname']
            update_customer.password = request.form['password']
            update_customer.email = request.form['email']
            update_customer.mobno = request.form['mobno']
            update_customer.address = request.form['address']
            update_customer.emergencyContact = request.form['emergencyContact']
            update_customer.emergencyName = request.form['emergencyName']
            update_customer.medicalHistory = request.form['medicalHistory']
            update_customer.age = request.form['age'] 
            update_customer.gender = request.form['gender']
            update_customer.aadharNo = request.form['aadharNo']
            update_customer.bloodGroup = request.form['bloodGroup']
            update_customer.policyNumber = request.form['policyNumber']
            update_customer.familyDoctorName = request.form['familyDoctorName']
            update_customer.familyDoctorContact = request.form['familyDoctorContact']
            db.session.commit()
            return render_template("readnfc.php", **{"details": customer.query.filter_by(username='20BRS1017').all()})
        except:
            return "there was some error to update the database"

@app.route("/readnfc.php")
def read():
    return render_template("readnfc.php", **{"details": customer.query.filter_by(username='20BRS1017').all()})

if __name__=="__main__":
    app.run(debug=True)
