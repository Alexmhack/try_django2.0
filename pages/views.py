from django.shortcuts import render
from django.http import HttpResponse


def homepage_view(request):
	return render(request, 'home.html', {})


def contact_view(request):
	return render(request, 'contact.html', {})


def about_view(request):
	context = {
		"about_number": 31121999,
		"about_us": "this is about us",
		"about_list": [10, 20, 30, 40],
		"about_html": "<h1>About Page At Page</h1>"
	}
	return render(request, 'about.html', context)


def social_view(request):
	return render()