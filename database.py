import pymongo
import sys


#Creating the database
myclient = pymongo.MongoClient("mongodb://localhost:27017") #Port number and IP combination
mydb = myclient["CEN434Database"]
mycol = mydb["Students"]

#------------Functions------------

#Select function to be performed


# Add a new record to the database
def add_new_record(mycol, record):
    result = mycol.insert_one(record)
    return result.inserted_id 

#Update the record of database

#Prompt the user for their details
name = input("Enter the student's name: ")
hall = input("Enter the student's hall: ") 
room = input("Enter the student's room: ")
matric_number = input("Enter the student's matric number: ")

#Create a new dictionary to store values
new_record = {
    "name": name,
    "hall": hall,
    "room": room,
    "matric-number": matric_number
  }
#Add the new record to the database.
new_record_id = add_new_record(mycol, new_record)

 # Print a confirmation message.
print("New record added successfully!")