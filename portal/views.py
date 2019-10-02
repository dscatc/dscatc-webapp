from django.core.checks import messages
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})

def checkin(request):
        return render(request, 'checkin.html')

