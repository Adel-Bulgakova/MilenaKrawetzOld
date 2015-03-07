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
        print response
        return render_to_response('portfolio/home.html', response, template.RequestContext(request))


def get_portfolio_list(request):
	response = {}
	portfolio = Portfolio.objects.all()
	full_objects = []
	for portfolio in portfolio:
		portfolio_images = Portfolio_image.objects.all()
		array_img = []
		for image in portfolio_images:
			portfolio_image = image.portfolio
			if portfolio == portfolio_image:
				img = image.image
				array_img.append(img)
		full_object = {'portfolio':portfolio, 'array_img':array_img}
		full_objects.append(full_object)

	response['portfolio'] = full_objects
	return render_to_response('portfolio/portfolio_list.html', response, template.RequestContext(request))