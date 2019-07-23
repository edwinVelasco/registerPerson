from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def return_view_admin(request):
    return HttpResponseRedirect('admin/login/')