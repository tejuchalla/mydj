from django.shortcuts import render
from django.http import HttpResponse

def simple(req):
    return HttpResponse('This sample page')
