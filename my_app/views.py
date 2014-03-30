# Create your views here.
#from django.http import HttpResponse

#def about(request):
#	return HttpResponse("<h1>About Us</h1>")

#def home(request):
#	return HttpResponse("<h1>Sample App</h1>")

#def help(request):
#	return HttpResponse("<h1>Help page</h1>")

#def index(request):
#	return HttpResponse("<h1>Index page</h1>")

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def home(request):
    return render_to_response('home.html')

def help(request):
    return render_to_response('help.html')

def about(request):
    return render_to_response('about.html')

def base(request):
    return render_to_response('base_index.html')