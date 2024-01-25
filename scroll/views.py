import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'scroll/index.html')

def posts(request):

	# Get start and end points
	start = int(request.GET.get('start') or 0)
	end = int(request.GET.get('end') or (start + 9))

	# Generate list of posts
	data = []
	for i in range(start, end + 1):
		data.append(f'Post #{i}')
	
	return JsonResponse({'posts' : data})