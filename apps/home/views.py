# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from random import randint

def about(request):
    return render(request, "home/about.html")

