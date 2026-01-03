from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templatesApp/index.html')

def nosotros(request):
    return render(request, 'templatesApp/about.html')