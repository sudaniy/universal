from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, About, Services, Project, Post, Team, Staff
from django.views.generic import DetailView, ListView

def home(request): 
    abouts = About.objects.all()
    slides = Slider.objects.all()
    services = Services.objects.all()[:6]
    gals = Project.objects.all()[:6]
    news = Post.objects.all()[:6]
    return render(request, 'website/index.html', {'slides':slides, 'abouts':abouts, 
                                                    'services':services, 'gals':gals, 'news':news})

def about(request):
    staffs = Staff.objects.all()
    abouts = About.objects.all()
    our_team = Team.objects.all()
    return render(request, 'website/about.html', {'abouts':abouts, 'our_team': our_team, 'staffs': staffs})

def project(request):
    gals = Project.objects.all()
    return render(request, 'website/projects.html', {'gals':gals})

def service(request):
    services = Services.objects.all()
    return render(request, 'website/services.html', {'services':services})

def news(request):
    news = Post.objects.all()
    return render(request, 'website/news.html', {'news':news})

def contact(request):
    return render(request, 'website/contact.html')

class NewsList(ListView):
    model = Post
    template_name = 'website/news.html'
    context_object_name = 'news'

class NewsDetails(DetailView):
    model = Post



                                                

