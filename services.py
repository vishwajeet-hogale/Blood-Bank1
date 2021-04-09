from app import db
import pymongo
import json
from bson.json_util import dumps
# mongo = pymongo.MongoClient("mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# db = mongo["Blood-Bank"]
def convert_donor_tuple(data):
	Donor_Data = pymongo.collection.Collection(db, 'Donor_Data')
	data = json.loads(dumps(Donor_Data.find()))
	all_result = []
	for i in data:
		temp = []
		temp.append(i["name"])
		temp.append(i["bloodgroup"])
		temp.append(i["address"])
	
		temp.append(i["phone"])
		all_result.append(temp)
	return all_result
def get_organization_by_email(email:str):
	Org_Data = pymongo.collection.Collection(db, 'Org_Data')
	data = json.loads(dumps(Org_Data.find({"email":email})))
	return data[0]["name"]
def get_all_donors_from_organization(email:str):
	org = get_organization_by_email(email)
	Donor_data = pymongo.collection.Collection(db, 'Donor_Data')
	data = json.loads(dumps(Donor_data.find({"organization":org})))
	return data
def get_donor_bloodgroup_by_email(email:str):
	donor = pymongo.collection.Collection(db,"Donor_Data")
	don = list(donor.find({"email":email}).limit(1))
	print(don)
	return don[0]["bloodgroup"]