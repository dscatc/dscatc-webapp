from django.shortcuts import render

# Create your views here.
# render check in view.
def check_in(request):
    return render(request, 'check_in.html', {})