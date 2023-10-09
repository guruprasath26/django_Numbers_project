
from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,"generator/index.html")
def number(request):
    c = list("0123456789")
    
    
    length = int(request.GET.get("length"))
    
 
    number = ""
    for x in range(length):
        number = number + random.choice(c)
    return render(request,"generator/password.html",{"number":number})