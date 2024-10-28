# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
import requests
from dotenv import load_dotenv
import requests
import json
from django_ratelimit.decorators import ratelimit


load_dotenv()

# Create your views here.
@ratelimit(key='ip', rate='5/m')
def index(request):
    if (request.method != 'POST'):
       return JsonResponse({
            "error": "Method not allowed",
            "message": "Only POST requests are supported for this endpoint",
            "success": False
        }, status=405)
    
    input_message = request.POST.get('message')
    tone = request.POST.get('tone')

    if not input_message or not tone:
        return JsonResponse({
            "error": "Missing parameters",
            "message": "Both 'message' and 'tone' are required",
            "success": False
        }, status=400)

    output = getLLMResponse(input_message, tone, "gpt-3.5-turbo")
    return JsonResponse({"data": output, "message": "Response successfully generated", "success" : True})

def getLLMResponse(inp, tone, llm="gpt-4o-mini"):
        openai_key = os.getenv("OPENAI_KEY")
        openai_url = 'https://api.openai.com/v1/chat/completions'

        system_prompt = "Analyze the input tone, style, and language patterns, then generate a casual, Gen-Z response that matches the intent and flows naturally with informal expressions or slang where fitting."

        user_prompt = f"{inp}"
        data = { "model": llm,
                "messages": [{"role": "system", "content": system_prompt},{"role": "user", "content": user_prompt}]
            }
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai_key}"}
        response = requests.post(openai_url, json=data, headers=headers)
        responsedata = response.json()
        output = responsedata['choices'][0]['message']['content']
        return output
