from django.shortcuts import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def hotel(request):
    if request.method == "POST":
       x = request.POST.get("city")
       print(x)

    return render(request,'hotel.html')

def contact(request):
    return render(request,'contact.html')

def flight(request):
    return render(request,'flight.html')

#    return render(request,'our.html')
