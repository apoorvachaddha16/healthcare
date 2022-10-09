from django.shortcuts import render
from django.template.context import RequestContext
# Create your views here.
def caresystem(request):
    return render(request, 'login.html')
