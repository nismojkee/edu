from django.shortcuts import render
from .models import news, course, reviewer
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

reviewers = reviewer.objects.all()

def index(request):
	return render(
		request,
		'index.html',
		{
			'title':'Home',
		}
	)

def review(request):
	return render(
		request,
		'review.html',
		{
			'reviews': reviewer.objects.all(),
			'title':'Reviews',
		}
	)

def review_leave(request):
	reviewers.create(
	    name = request.POST['reviewer_name'],
	    email = request.POST['reviewer_mail'],
	    review = request.POST['reviewer_message'],
	    photo = request.FILES['files[]'],
	    created = timezone.now()
	)
	return HttpResponseRedirect( reverse('review') )