# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from models import Art
from django.views.generic import ListView, DetailView

# def portfolio(request):
# 		return render(request, "portfolio/portfolio.html")

class pictures_list_view(ListView):
    model = Art

class picture_detail_view(DetailView):
    model = Art