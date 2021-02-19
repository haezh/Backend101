from django.shortcuts import render
from django.http import HttpResponse
from .models import Name

# Create your views here.
# What we show to API calls

def index(request, first_name):
    names = Name.objects.filter(first_name = first_name)
    if len(names) > 0:
        name = names[0]
        return HttpResponse("Hello, grils. You're at the names index page. The last name you are looking for is :" + name.last_name)
    else:
        return HttpResponse("Hello, grils. You're at the names index page. The name is not found in system")