from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects #queryset
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details' : details})

def cheer(request):
    return render(request, 'cheer.html')

def create(request):
     blog = Blog()
     blog.title = request.GET['title']
     blog.body = request.GET['body']
     blog.pub_date = timezone.datetime.now()
     blog.save()
     return redirect('/blog/cheer')

def calendar(request):
    return render(request, 'calendar.html')