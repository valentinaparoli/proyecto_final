from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def listado_de_calas(request):
    return render(request, 'home/calas.html')