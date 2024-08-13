from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Address

# Create your views here.


def index(request):
    response = HttpResponse('Hello API!!!')
    return response

def cities(request):
    cities = Address.objects.values('city').distinct()
    cities = [item['city'] for item in cities]
    return JsonResponse(cities, safe=False)

def districts(request, city_name):
    # distinct 可以並免獲取重複資料
    districts = Address.objects.filter(city=city_name).values('site_id').distinct()
    print(districts)
    districts = [item['site_id'] for item in districts]
    return JsonResponse(districts, safe=False)
