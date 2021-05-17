# Write a function in python for :
# 1) Inserting 5 student's details such as first_name, last_name, dob, class, roll_no.
#
# 2) Finding the deatils of any one student by his roll_no.
#
# 3) delete a student whose roll_no is 4
#
# 4) update a student's dob whose roll no is 3.

import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")  # Python platform Create connection with Mongodb Compass
mydb=myclient['School']
print(myclient.list_database_names())

mycol = mydb["Student"]
# mydict = [{ "First_name": "Shruti", "Last_Name": "Kumari",'DOB':"11-11-1997",'Class':'10th',"Roll_No":1},
#           { "First_name": "Rahul", "Last_Name": "Kumar",'DOB':"11-12-1998",'Class':'11th',"Roll_No":2 },
#           { "First_name": "Shubham", "Last_Name": "Kumar",'DOB':"11-7-1999",'Class':'11th',"Roll_No":3 },
#           { "First_name": "Manu", "Last_Name": "Kumari",'DOB':"11-11-1990",'Class':'10th',"Roll_No":4 },
#           { "First_name": "Anu", "Last_Name": "Kumari",'DOB':"11-11-1999",'Class':'10th',"Roll_No":5}
#           ]
# x = mycol.insert_many(mydict)
for x in mycol.find():
    print(x)

