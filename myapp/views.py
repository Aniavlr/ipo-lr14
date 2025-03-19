from django.shortcuts import render, HttpResponse

# Create your views here.

def main_page(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def ofiston(request):
    return render(request, 'ophiston.html')
