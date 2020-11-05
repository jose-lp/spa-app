from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(
        request,
        'index.html'
    )

def new(request):
    return HttpResponse('Showing "new" page')

def delete(request):
    return HttpResponse('Showing "delete" page')

def check(request):
    return HttpResponse('Showing "check" page')
