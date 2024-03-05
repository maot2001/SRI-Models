from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import sys

# current_route = os.path.dirname(os.path.abspath(__file__))
# prev_route = os.path.join(current_route, "..", "code")
# sys.path.append(prev_route)
# import boolean

def finder(request):
    context = {
        'project_name':'SRI-Models'
    }
    return render(request, 'finder.html', context)

def hello_function(request):
    if request.method == 'POST':
        print("hello_funcion entrando")
        data = json.loads(request.body)
        query = data.get('query','')
        is_boolean = data.get('is_boolean','')
        #ver como coger los datos del back
        result = ["A","B","V","kfjkajfkjakf", "sfjaskfjal","safldadsf","shfeuireiorum,c", "sjfkasjfk","ksjfkasjf","sjfkasjfksa","kjdsfkjaskfj","kjfsakfjaskfj","ksjfkajskf","Z","skflaskf","xsacassd","ksfkasjfksajf","klsafklaskf"]
        return JsonResponse({'result':result})
    else: 
        return HttpResponse(status=400)
    
def result(request):
    return JsonResponse({"result":"hello"})
