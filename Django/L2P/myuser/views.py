from django.shortcuts import render
from myuser.models import User_details
from myuser import forms

# Create your views here.
def index(request):
    return render(request, "myuser/index.html")

def add_user(request):
    f = forms.SForm()
    if request.method == 'POST':
        f = forms.SForm(request.POST)
        f.save(commit = True)
        return index(request)
    # if request.method == 'POST':
    #     f = forms.SForm(request.POST)
    #     if f.is_valid():
    #         f.save(commit = True)
    #         return index(request)
    #     else:
    #         print('ERROR FORM INVALID')
    return render(request, "myuser/user.html", {'form' : f})

def help(request):
    users = User_details.objects.order_by('first_name')
    my_dict = {'user_insert' : users}
    return render(request, "myuser/users.html", context = my_dict)
