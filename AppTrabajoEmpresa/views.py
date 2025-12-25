from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'templatesApp/index.html')

def inicio2(request):
    return render(request, 'templatesApp/propuesta2.html')