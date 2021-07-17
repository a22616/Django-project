from django.shortcuts import render
from boking.models import HOTEL,FLIGHT,CONTACT
# Create your views here.
def home(request):
    return render(request,'home.html')

def hotel(request):
    if request.method == "POST":
       x = request.POST.get("name")
       f = request.POST.get("city")
       y = request.POST.get("fromDate")
       z = request.POST.get("toDate")
       a = request.POST.get("rooms")
       b = request.POST.get("adults")
       c = request.POST.get("children")
       d = request.POST.get("email")
       e = request.POST.get("Phone")

       hotels = HOTEL(name=x,city=f,from_date=y,to_date=z,rooms=a,adults=b,children=c,email=d,Phone=e)
       hotels.save()
    #    print([x,y,z,a,b,c,d,e,f])

    return render(request,'hotel.html')

def contact(request):
    if request.method == "POST":
        x = request.POST.get("name")
        y = request.POST.get("Phone")
        z = request.POST.get("email")

        contacts = CONTACT(name=x,Phone=y,email=z)
        contacts.save()
        # print([x,y,z])

    return render(request,'contact.html')

def flight(request):
    if request.method == "POST":
        x = request.POST.get("name")
        y = request.POST.get("gender1")
        a = request.POST.get("from")
        b = request.POST.get("to")
        c = request.POST.get("fromDate")
        d = request.POST.get("toDate")
        e = request.POST.get("rooms")
        f = request.POST.get("adults")
        g = request.POST.get("children")
        
        flights = FLIGHT(name=x,gender1=y,from_city=a,to_city=b,from_date=c,to_date=d,rooms=e,adults=f,children=g)
        flights.save()
        # print([x,y,a,b,c,d,e,f,g])

    return render(request,'flight.html')
