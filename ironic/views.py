from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# If it's a post request, get the information and make a http response to an api and then return the contents of it inside HTTPResponse()
def index(request):
    if (request.method == 'GET'):
        return render(request, "ironic/index.html")
    else:
        
        print('bro wtf')
        return HttpResponse("ayo")