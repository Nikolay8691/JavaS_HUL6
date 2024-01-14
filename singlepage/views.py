from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def hello(request, name):
	return HttpResponse(f' glad to see you, {name.capitalize()}, and hello from the JS_Singlepage_app! ')