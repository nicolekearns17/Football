from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from fcoupon.models import Category, Page, UserProfile

def index(request):
	context = RequestContext(request)
	category_list = Category.objects.all()
	context_dict = {'categories': category_list}
	return render_to_response('fcoupon/index.html', context_dict)
