from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'async await'
    return render(request, 'home/index.html', locals())

def json_demo(request):
    title = 'JSON 練習'
    return render(request, 'home/json.html', locals())