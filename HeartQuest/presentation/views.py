from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'presentation/index.html')

def logout(request):
    return render(request, 'presentation/index.html')