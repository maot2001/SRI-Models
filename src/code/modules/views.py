from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json


def finder(request):
    context = {
        'project_name':'SRI-Models'
    }
    return render(request, 'finder.html', context)

def hello_function(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query','')
        result = query.upper()
        return JsonResponse({'result':result})
    else: 
        print('GET PERRO HELLO_FUNCTION')
        return HttpResponse(status=400)
