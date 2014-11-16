# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from models import Post
from django.views.generic import ListView, DetailView

def blog(request):
		return render(request, "blog/blog.html")

class posts_list_view(ListView):
    model = Post

class post_detail_view(DetailView):
    model = Post

