from django.http import HttpRespomnse
from django.shortcuts import render

# Create your views here.
def index(request):

    return HttpRespomnse("Thanks for surfing us out of all those websites around !")