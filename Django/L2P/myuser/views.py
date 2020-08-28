from django.shortcuts import render
from myuser.models import User_details
# Create your views here.
def index(request):
    my_dict = {'index_insert' : "Go to /help to check user data"}
    return render(request, "myuser/index.html", context = my_dict)

def help(request):
    users = User_details.objects.order_by('first_name')
    my_dict = {'user_insert' : users}
    return render(request, "myuser/users.html", context = my_dict)
