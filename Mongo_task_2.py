import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")  # Python platform Create connection with Mongodb Compass
mydb=myclient['School']
mycol = mydb["Student"]

# 2) Finding the deatils of any one student by his roll_no.
# for x in mycol.find({'Roll_No':2}):
#     print(x)

# 3) delete a student whose roll_no is 4
# mycol.remove({"Roll_No":4},1)
#
# for x in mycol.find():
#     print(x)

# 4) update a student's dob whose roll no is 3.
# mycol.update({"Roll_No":3},{"DOB":"10-10-1995"})
# for x in mycol.find():
#     print(x)

#mycol.remove({"DOB":'10-10-1995'})

# mydata={ "First_name": "Shubham", "Last_Name": "Kumar",'DOB':"11-7-1999",'Class':'11th',"Roll_No":3 }
# mycol.insert_one(mydata)
#
# for x in mycol.find():
#     print(x)

mycol.update({'Roll_No':3},{ "$set": { "DOB": "10-10-1999" } })

for x in mycol.find():
    print(x)
