from django.http import HttpResponse

def home_page(request):
    return HttpResponse("this is a home page")

def login_view(request):
    return HttpResponse("this is a login page")
    