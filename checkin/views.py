from django.shortcuts import render, redirect

# Create your views here.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# Message from harsh borse to developers only....scope is auth checker,,
# it may vary time to time...
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name("checkin-creds.json", scope)

# client = gspread.authorize(creds)

# sheet = client.open("Contact Information (Responses)").sheet1  # Open the spreadhseet

# data = sheet.get_all_records()  # Get a list of all records as dictionary formate in a list

# pprint(data)

# fields  = sheet.get_all_values() # get all the data into a list formate

# print("You have these Columns\n",fields[0]) #printing the column names

# print("\n\nand data entered are \n\n")

# printing the data entered by people
# for i in range(1,len(fields)):
#     print(fields[i])

# tuples = sheet.row_values()


def checkinGen(request):
    print("\n\n\n____________________________________________________________________________________________________")
    print("checkin gen")
    print("START\n\n")
    creds = ServiceAccountCredentials.from_json_keyfile_name("checkin/checkin-creds.json", scope)
    client = gspread.authorize(creds)
    filename = request.POST['filename']
    sheet = client.open(filename).sheet1 # Open the spreadhseet
    fields = sheet.get_all_values()  # get all the data into a list formate

    print("You have these Columns\n", fields[0])  # printing the column names

    print("\nand data entered are\n")

    # printing the data entered by people
    for i in range(1, len(fields)):
        print("\n")
        print(fields[i])

    print("\n\n END")
    print("____________________________________________________________________________________________________\n\n\n")
    return redirect('/checkin')
