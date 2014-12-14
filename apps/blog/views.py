# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from models import Post, Post_image
# from django.views.generic import ListView, DetailView
from django import template


def get_posts_list(request):
	response = {}
	response['posts'] = Post.objects.all()
	return render_to_response('portfolio/post_list.html', response, template.RequestContext(request))


def get_post_detail(request):
	response = {}
	response['post'] = None
	response['posts'] = Post.objects.filter(products__isnull=False).distinct()
	return render_to_response('portfolio/post_detail.html', response, template.RequestContext(request))


def get_images(request):

    # image = Post_image.objects.filter(post_image_id=id).order_by('-id')
    image = Post_image.objects.select_related('image')
    return render_to_response('portfolio/post_list.html', {"image": image}, template.RequestContext(request))



# class posts_list_view(ListView):
#     model = Post
#
# class post_detail_view(DetailView):
#     model = Post

