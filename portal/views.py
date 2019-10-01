from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

# to render the check in page assuming that it is created
def check_in(request):
    return render(request, 'checkin.html', {})