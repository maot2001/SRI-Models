from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import sys
current_route = os.path.dirname(os.path.abspath(__file__))
prev_route = os.path.join(current_route, "..", "code")
sys.path.append(prev_route)
import boolean
import utils
import query_lsi

data_words = utils.json_to_words()
data_docs = utils.json_to_doc()

def finder(request):
    context = {
        'project_name':'SRI-Models'
    }
    return render(request, 'finder.html', context)

def hello_function(request):
    global data_words, data_docs
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query','')
        is_boolean = data.get('is_boolean','')
        if is_boolean:
            result = boolean.get_matching_docs(query,data_words,data_docs)[0]
            print(result)
        else: 
            result = [tup[0] for tup in query_lsi.query_lsi(query, data_words, data_docs)]
            print(result)
        return JsonResponse({'result':result})
    else: 
        return HttpResponse(status=400)
    
def result(request):
    return JsonResponse({"result":"hello"})
