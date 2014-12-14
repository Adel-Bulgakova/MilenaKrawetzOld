# encoding: utf-8
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from forms import ContactForm
from models import Contact
from django.template import RequestContext
from django.core.mail import send_mail

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			author_name = form.cleaned_data['author_name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			message_title = 'Message from MilenaKrawetz.com'
			send_mail(message_title, message, 'davletshina.adel@gmail.com', ['davletshina.adel@gmail.com'])

			contact = Contact(author_name = author_name, email = email, message = message)
			contact.save()
			return HttpResponseRedirect('/contact/')
	else:
		form = ContactForm()
	return render_to_response('contact/contact.html', {'form': form}, RequestContext(request))