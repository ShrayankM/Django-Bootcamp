from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage

# Create your views here.
def index(request):
    webpages = Webpage.objects.order_by('name')
    my_dict = {'webpage_table' : webpages}
    return render(request, 'first_app/index.html', context = my_dict)
