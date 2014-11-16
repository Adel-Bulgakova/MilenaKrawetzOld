# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from random import randint

def home(request):
    if request.method == "GET":
        return render(request, "home/home.html")

def about(request):
    print "dx"
    return render(request, "home/about.html")

