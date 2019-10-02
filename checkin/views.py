from django.shortcuts import render, redirect
from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Create your views here.
# render check in view.
def check_in(request):
    if request == 'POST':
        checkinGen(request)
    else:
        return render(request, 'check_in.html', {})


def checkinGen(request):
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
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