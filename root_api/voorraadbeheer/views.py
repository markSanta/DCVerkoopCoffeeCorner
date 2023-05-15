from django.http import JsonResponse

from .models import Product

def index(request):
    # important: convert the QuerySet to a list object
    data = list(Product.objects.all().values()) 
    return JsonResponse(data, safe=False)
