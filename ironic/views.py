from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from dotenv import load_dotenv
import requests
import json
from .ml import isIronic
from django_ratelimit.decorators import ratelimit

load_dotenv()

# Create your views here.
# If it's a post request, get the information and make a http response to an api and then return the contents of it inside HTTPResponse()
@ratelimit(key='ip', rate='5/m')
def index(request):
    if (request.method != 'POST'):
       return JsonResponse({
            "error": "Method not allowed",
            "message": "Only POST requests are supported for this endpoint",
            "success": False
        }, status=405)
    
    input_message = request.POST.get('message')

    if not input_message:
        return JsonResponse({
            "error": "Missing parameters",
            "message": "'message' is required",
            "success": False
        }, status=400)

    output = isIronic(input_message)
    print(output)
    return JsonResponse({"tone": {
        "type" : "ironic", "value" : str(output)
    }, "message": "Response successfully generated", "success" : True})

