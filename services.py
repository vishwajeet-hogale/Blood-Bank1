from app import db
import pymongo
import json
from bson.json_util import dumps
# mongo = pymongo.MongoClient("mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
import re
# db = mongo["Blood-Bank"]
blood_groups = ["A","B","O","AB"]
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

def get_donor_by_email(email:str):
	data = pymongo.collection.Collection(db,'Donor_Data')
	donor = list(data.find({"email":email}))
	if(donor == []):
		return True
	return False
def get_org_by_email_for_duplicate(email:str):
	data = pymongo.collection.Collection(db,'Org_Data')
	org = list(data.find({"email":email}))
	if(org == []):
		return True
	return False
def check_for_valid_bloodgroup(group:str):
	for i in blood_groups:
		if(group[0].strip().upper() == i):
			return True
	return False
def check_for_valid_email(email:str):
	regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
	if(re.search(regex, email)):
		return True
	return False
def check_for_valid_phno(number:str):
	if len(number) == 10:
		return True
	return False
