from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
	return JsonResponse({"Message": "Hello World!"})
def hello(request):
	return render(request, 'hello.html')
