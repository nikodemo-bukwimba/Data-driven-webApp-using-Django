from django.shortcuts import render

#Return webpage according to user request.
def home(request):
    name = "Mwl.luhondo"
    return render(request,"home.html",{"name":name})
