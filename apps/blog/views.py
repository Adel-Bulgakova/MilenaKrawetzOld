# encoding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from models import Post, Post_image
from django import template


def get_posts_list(request):
	response = {}
	posts = Post.objects.all()
	full_objects = []
	for post in posts:
		post_images = Post_image.objects.all()
		array_img = []
		for image in post_images:
			if post == image.post:
				img = image.image
				array_img.append(img)

		full_object = {'post':post, 'img':array_img[0]}
		full_objects.append(full_object)

	response['posts'] = full_objects
	return render_to_response('blog/post_list.html', response, template.RequestContext(request))


def get_post_detail(request, pk):
    response = {}
    post = get_object_or_404(Post, pk=pk)
    post_images = Post_image.objects.all()
    array_img = []
    for image in post_images:
        if post == image.post:
            array_img.append(image)
    post.content = parse_content(post.content, array_img)
    full_object = {'post':post, 'array_img':array_img}
    response['post'] = full_object
    return render_to_response('blog/post_detail.html', response, template.RequestContext(request))


def parse_content(content, array_img):
    result = ''
    while content.find('##')>0:
        s = content[0:content.find('##')]
        p = "<p>"+ s + "</p>"
        content = content.replace(content[:content.find('##')+2], '')
        id = content[0:(content.find('$$'))]
        array_group_of_images = get_group_of_images(id, array_img)
        div = get_div(id, array_group_of_images)
        content = content.replace(content[:content.find('$$')+2], '')
        result += p + div
    p = "<p>"+ content + "</p>"
    return result+p

def get_group_of_images(id, array_img):
    array_group_images = []
    for image in array_img:
         if id == image.image_group:
             array_group_images.append(image.image)
    return array_group_images

def get_div (id, array_group_of_images):
    images = ''
    for image in array_group_of_images:
        images += "<img src='/media/"+ image.name + "'>"
        div = "<div class = 'image_in_post'><div id = '"+ id + "' class = 'fotorama' data-allowfullscreen = 'true' data-width = '700' data-ratio = '700/467' data-max-width = '100%'>"+ images+"</div></div>"
    return div

