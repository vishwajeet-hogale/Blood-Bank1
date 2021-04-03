import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import base64
import requests
import random

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = b'\xd2(*K\xa0\xa8\x13]g\x1e9\x88\x10\xb0\xe0\xcc'

#Loads the Database and Collections
mongo = pymongo.MongoClient("mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = mongo["Blood-Bank"]

#Home page
@app.route('/')
def home_page():
	return render_template('index.html')

#Map page
@app.route('/map')
def map_page():
	return render_template('homepage.html')

#Add new User
@app.route('/add_new_user', methods=['POST'])
def add_new_user():
    inputData = dict(request.form)
    Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
    Donor_Data.insert_one(inputData)
    return Response(status=200)

#Org landing page
@app.route('/org_lander')
def org_lander():
    return render_template('orglander.html')

#Add new org
@app.route('/add_new_org', methods=['POST'])
def add_new_org():
    Org_Data = pymongo.collection.Collection(db, 'Org_Data')
    inputData = dict(request.form)
    for i in json.loads(dumps(Org_Data.find())):
        if i['email'] == inputData['email']:
            return Response(status=304)
    Org_Data.insert_one(inputData)
    return Response(status=200)

#Add new alert
@app.route('/add_new_alert', methods=['POST'])
def add_new_alert():
	Alert_Data = pymongo.collection.Collection(db, 'Alert_Data')
	inputData = dict(request.form)
	Alert_Data.insert_one(inputData)
	return Response(status=200)

#Get alert data
@app.route('/get_alert', methods=['POST'])
def get_alert():
	Alert_Data = pymongo.collection.Collection(db, 'Alert_Data')
	data = json.loads(dumps(Alert_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1

#Add new drive
@app.route('/add_new_drive', methods=['POST'])
def add_new_drive():
	Drive_Data = pymongo.collection.Collection(db, 'Drive_Data')
	inputData = dict(request.form)
	Drive_Data.insert_one(inputData)
	return Response(status=200)

#Get drives
@app.route('/get_drive', methods=['POST'])
def get_drive():
	Drive_Data = pymongo.collection.Collection(db, 'Drive_Data')
	data = json.loads(dumps(Drive_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1

#Get donors
@app.route('/get_donors', methods=['POST'])
def get_donors():
	Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
	data = json.loads(dumps(Donor_Data.find()))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	return data1

#Org login
@app.route('/org_login', methods=['POST'])
def org_login():
	Org_Data = pymongo.collection.Collection(db, 'Org_Data')
	inputData = dict(request.form)
	for i in json.loads(dumps(Org_Data.find())):
		if i['email'] == inputData['email'] and i['password'] == inputData['password']:
			session['email'] = inputData['email']
			return render_template('orgdashboard.html')
	return Response(status=403)

#Org landing page
@app.route('/org_dash')
def org_dash():
    return render_template('orgdashboard.html')

@app.route('/add_new_patient', methods=['POST'])
def add_new_patient():
	print("Hello")
	inputData = dict(request.form)
	patient_Data = pymongo.collection.Collection(db, 'Patient_data')
	patient_Data.insert_one(inputData)
	return Response(status=200)


@app.route("/pat_login",methods = ["POST"])
def patient_login():
	if request.method == "POST":
		Org_Data = pymongo.collection.Collection(db, 'Patient_data')
		inputData = dict(request.form)
		for i in json.loads(dumps(Org_Data.find())):
			if i['email'] == inputData['email'] and i['password'] == inputData['password']:
				session['email'] = inputData['email']
				return render_template("orgdashboard.html")
		return Response(status=403)
	


if __name__=="__main__":
	app.run(debug=True)