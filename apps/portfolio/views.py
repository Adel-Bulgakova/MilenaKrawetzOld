# encoding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from models import Portfolio, Portfolio_image
from django import template
from random import randint


def get_random_images(request):
    if request.method == "GET":
        response = {}
        random_works = Portfolio.objects.order_by('?')[:5]
        full_objects = []
        for work in random_works:
            pictures = Portfolio_image.objects.all()
            for picture in pictures:
                if work == picture.portfolio:
                    full_object = {'portfolio':work, 'image':picture.image}
                    full_objects.append(full_object)
        response['portfolio'] = full_objects
        return render_to_response('portfolio/home.html', response, template.RequestContext(request))


def get_portfolio_list(request):
	response = {}
	works = Portfolio.objects.all()
	full_objects = []
	for work in works:
		pictures = Portfolio_image.objects.all()
		work_images = []
		for picture in pictures:
			if work == picture.portfolio:
				work_image = picture.image
				work_images.append(work_image)
		full_object = {'portfolio':work, 'work_images':work_images}
		full_objects.append(full_object)

	response['portfolio'] = full_objects
	return render_to_response('portfolio/portfolio_list.html', response, template.RequestContext(request))