import pymongo
import sys


# Creating the database
myclient = pymongo.MongoClient("mongodb://localhost:27017")  # Port number and IP combination
mydb = myclient["CEN434Database"]
mycol = mydb["Students"]
collection = mydb["People"]

# ------------Functions------------

# Add a new record to the database
def add_new_record(mycol, record):
  result = mycol.insert_one(record)
  return result.inserted_id

# Update the record of the database
def update_record(mycol, filter_query, update_query):
  result = mycol.update_one(filter_query, update_query)
  return result.modified_count
#------------Functions------------

# Select function to be performed
choice = input("Select function to be performed (update/create): ")

if choice == "update":
  # Prompt the user for their details
  name = input("Enter the student's name: ")
  hall = input("Enter the student's hall: ")
  room = input("Enter the student's room: ")
  matric_number = input("Enter the student's matric number: ")

  # Update the record of database
  filter_query = {"name": name}  # Example filter query
  update_query = {"$set": {"hall": hall, "room": room, "matric-number": matric_number}}  # Example update query
  update_record(mycol, filter_query, update_query)
  print("Record updated successfully!")
elif choice == "create":
  # Prompt the user for their details
  name = input("Enter the student's name: ")
  hall = input("Enter the student's hall: ")
  room = input("Enter the student's room: ")
  matric_number = input("Enter the student's matric number: ")

  # Create a new dictionary to store values
  new_record = {
    "name": name,
    "hall": hall,
    "room": room,
    "matric-number": matric_number
  }
  # Add the new record to the database.
  new_record_id = new_record(mycol, new_record)
  print("New record added successfully!")
else:
  print("Invalid choice!")



# Add a new record to the database
def add_new_record(mycol, record):
    result = mycol.insert_one(record)
    return result.inserted_id 

# Update the record of database
def update_record(mycol, filter_query, update_query):
  result = mycol.update_one(filter_query, update_query)
  return result.modified_count


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