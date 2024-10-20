from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
import requests

load_dotenv()

# Create your views here.
# If it's a post request, get the information and make a http response to an api and then return the contents of it inside HTTPResponse()
def getLLMResponse(inp, llm="gpt-4o-mini"):
        openai_key = os.getenv("OPENAI_KEY")
        openai_url = 'https://api.openai.com/v1/chat/completions'
        data = { "model": llm,
                "messages": [{"role": "user", "content": inp}]
            }
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai_key}"}
        response = requests.post(openai_url, json=data, headers=headers)
        responsedata = response.json()
        output = responsedata['choices'][0]['message']['content']
        print(llm)
        return output


def index(request):
    if (request.method == 'GET'):
        return render(request, "ironic/index.html")
    else:
        input = request.POST.get('message')
        output = getLLMResponse(input, "gpt-3.5-turbo")
        print(output)
        return HttpResponse(f"the output is: {output}")
    

