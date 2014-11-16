# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from portfolio.models import Art, Post
from random import randint

def home(request):
	if request.method == "GET":
		return render(request, "portfolio/home.html")

def about(request):
		return render(request, "portfolio/about.html")

def portfolio(request):
		return render(request, "portfolio/portfolio.html")

def blog(request):
		return render(request, "portfolio/blog.html")

def shop(request):
		return render(request, "portfolio/shop.html")

def contact(request):
		return render(request, "portfolio/contact.html")