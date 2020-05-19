from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django import forms
from .models import Job
from accounts.models import Company

# Create your views here.

def about(request):
    
    return render(request, 'about.html')

def contact(request):

    return render(request,'contact.html')

def index(request):

    return render(request,'index.html')

def rainbow_tick(request):

    return render(request,'rainbow_tick.html')

def search_result(request):

    jobs = serializers.serialize('json', Job.objects.all())
    companies = serializers.serialize('json', Company.objects.all())

    # http://127.0.0.1:8000/static/pages/BallaratCommunityHealth.html

    return render(request,'search-result.html', {'jobs': jobs, 'companies': companies})

def blog(request):

    return render(request,'blog.html')

def new_post(request):

    return render(request,'new-post.html')

def job_post(request):

    return render(request,'job-post.html')

def job_single(request):

    return render(request,'job-single.html')

def profile(request):

    return render(request,'profile.html')

def organisation(request):

    return render(request,'organisation.html')

def test(request):

    
    str1 = str(request.GET["companyname"])
    str2 = str(request.GET["jobtype"])
    str3 = str(request.GET["loc"])
    data = Job.objects.filter(job_type=str2)
    data_dir = {'job':data, 'companyname':str1,'jobtype':str2,'loc':str3}
    return render(request, 'testforbackend.html', context=data_dir) 

def test1(request):

    data = Company.objects.all()
    data_dir = {'company':data}
    return render(request, 'testforbackend-company.html', context=data_dir) 
