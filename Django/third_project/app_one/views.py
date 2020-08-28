from django.shortcuts import render

# Create your views here.
def index(request):
    myDict = {'insert_content' : "Hello Im from app_one!!!"}
    return render(request, "app_one/index.html", context = myDict)

def page_one(request):
    myDict = {'insert_page_one' : "This is page One of app_one!!!"}
    return render(request, "app_one/pageOne.html", context = myDict)
