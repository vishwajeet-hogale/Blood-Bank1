import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, g,url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import services as sc
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
	if(sc.check_for_valid_bloodgroup(inputData["bloodgroup"]) and sc.check_for_valid_email(inputData["email"]) and sc.check_for_valid_phno(inputData["phone"])):
		if sc.get_donor_by_email(inputData["email"]) :
			Donor_Data.insert_one(inputData)
			return Response(status=200)
		# print("Already exists!")
		return Response(status=304)
	return Response(status=403)
@app.before_request  #The before_request decorator allows us to create a function that will run before each request.
def before_request():
    g.email = None
    if 'email' in session:
        g.email = session["email"] 
@app.route("/signout") #Helps you end the session i.e logs you out
def signout():
    session.pop("email",None)
    return redirect(url_for("org_lander"))
#Org landing page
@app.route('/org_lander')
def org_lander():
    return render_template('orglander.html')

#Add new org
@app.route('/add_new_org', methods=['POST'])
def add_new_org():
    Org_Data = pymongo.collection.Collection(db, 'Org_Data')
    inputData = dict(request.form)
	if(sc.check_for_valid_email(inputData["email"]) and sc.check_for_valid_phno(inputData["phone"]):)
		for i in json.loads(dumps(Org_Data.find())):
			if i['email'] == inputData['email']:
				return Response(status=304)
		Org_Data.insert_one(inputData)
		return Response(status=200)
	return Response(status=403)

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

# #Get donors
# @app.route('/get_donors', methods=['POST'])
# def get_donors():
# 	Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
# 	data = json.loads(dumps(Donor_Data.find()))
# 	data1 = {}
# 	y = 0
# 	data1['count'] = 0
# 	for x in data:
# 		data1["record"+str(y)] = x
# 		y+=1
# 	data1['count'] = y
# 	return data1
@app.route('/get_donors', methods=['POST'])
def get_donors():
    Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
    Org_Data = pymongo.collection.Collection(db, 'Org_Data')
    doc=list(Org_Data.find({"email":session["email"]}).limit(1))
    print(doc)
    data = json.loads(dumps(Donor_Data.find({"organization":doc[0]["name"]})))
    data1 = {}
    y = 0
    data1['count'] = 0
    for x in data:
        data1["record"+str(y)] = x
        y+=1
    data1['count'] = y
    return data1
#search_catalogue
@app.route("/get_bloodgroup",methods=["POST"])
def get_bloodgroup():
	blood_unit = pymongo.collection.Collection(db, 'Bloodunit')
	org = sc.get_organization_by_email(session["email"])
	data = json.loads(dumps(blood_unit.find({"org":org})))
	data1 = {}
	y = 0
	data1['count'] = 0
	for x in data:
		data1["record"+str(y)] = x
		y+=1
	data1['count'] = y
	print(data1)
	return data1
#Org login
@app.route('/org_login', methods=['POST',"GET"])
def org_login():
	if request.method == "POST":
		Org_Data = pymongo.collection.Collection(db, 'Org_Data')
		inputData = dict(request.form)
		donor = []
		for i in json.loads(dumps(Org_Data.find())):
			if i['email'] == inputData['email'] and i['password'] == inputData['password']:
				session['email'] = inputData['email']
				print(session["email"])
				org = sc.get_organization_by_email(session["email"])
				return render_template('orgdashboard.html',org=org)
	if(session["email"]):
		org = sc.get_organization_by_email(session["email"])
		return render_template('orgdashboard.html',org=org)
	return Response(status=403)

#Org landing page
@app.route('/org_dash')
def org_dash():
	if g.email:
		return render_template("orgdashboard.html")
	return render_template('orglander.html')

@app.route('/add_new_patient', methods=['POST'])
def add_new_patient():
	print("Hello")
	inputData = dict(request.form)
	patient_Data = pymongo.collection.Collection(db, 'Patient_data')
	patient_Data.insert_one(inputData)
	return Response(status=200)



@app.route("/accepted/<email>",methods=["GET","POST"])
def accepted(email):
	if request.method == "POST":
		pass
	
	all_donors = sc.get_all_donors_from_organization(session["email"])
	return render_template("donor.html",email = session["email"])
# @app.route("/add_blood",methods=["POST"])
# def add_blood():
# 	# print(email)
# 	inputData = dict(request.form)
# 	Bloodunit_Data = pymongo.collection.Collection(db, 'Bloodunit')
# 	type_of_blood = sc.get_donor_bloodgroup_by_email(email=inputData["email"])
# 	print(type_of_blood)
# 	b = list(Bloodunit_Data.find({"type":type_of_blood}).limit(1))
# 	if(b == []):
		
# 		Bloodunit_Data.insert_one({"units":int(inputData["units"]),"type":type_of_blood})
# 		return Response(status=200)
# 	else:

# 		old_val = int(b[0]["units"])
		
# 		query = {"units":int(b[0]["units"]),"type":type_of_blood}
# 		new_update = {"$set":{"units":old_val+int(inputData["units"])}}
# 		Bloodunit_Data.update_one(query,new_update)
# 		return Response(status=200)
# 	return Response(status=403)
@app.route("/add_blood",methods=["POST"])
def add_blood():
    # print(email)
    inputData = dict(request.form)
    Bloodunit_Data = pymongo.collection.Collection(db, 'Bloodunit')
    type_of_blood = sc.get_donor_bloodgroup_by_email(email=inputData["email"])
    print(type_of_blood)
    Org_Data = pymongo.collection.Collection(db, 'Org_Data')
    doc=list(Org_Data.find({"email":session["email"]}).limit(1))
    b = list(Bloodunit_Data.find({"type":type_of_blood,"org":doc[0]["name"]}).limit(1))
    print(b)
    if(b == []):

        Bloodunit_Data.insert_one({"units":inputData["units"],"type":type_of_blood,"org":inputData["org"]})
        return Response(status=200)
    else:

        old_val = int(b[0]["units"])

        query = {"units":b[0]["units"],"type":type_of_blood,"org":inputData["org"]}
        new_update = {"$set":{"units":old_val+int(inputData["units"])}}
        Bloodunit_Data.update_one(query,new_update)
        return Response(status=200)
@app.route("/donate_blood/<email>")
def donate_blood(email):
    return render_template("subtract.html",name = email)

@app.route("/subtract_blood",methods=["POST"])
def subtract_blood():
	inputData = dict(request.form)
	blood_unit = pymongo.collection.Collection(db,'Bloodunit')
	org = sc.get_organization_by_email(session["email"])
	b = list(blood_unit.find({"type":inputData["type"],"org":org}).limit(1))
	if(b == []):
		print("Blood not available")
		return Response(status=403)
	else:
		print(b[0])
		old_val = int(b[0]["units"])
		if(old_val >= int(inputData["units"])):
			query = {"units":int(b[0]["units"]),"type":inputData["type"],"org":org}
			new_update = {"$set":{"units":old_val-int(inputData["units"])}}
			blood_unit.update_one(query,new_update)
			return Response(status=200)
		else:
			print("You will only get a part of the blood! Search for another organization")
			return Response(status=403)


	
	
if __name__=="__main__":
	app.run(debug=True)