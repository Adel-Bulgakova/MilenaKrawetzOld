# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from models import Contact
from random import randint

def contact(request):
		return render(request, "contact/contact.html")