from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from datetime import date
from .models import Blog
# Create your views here.

def home_page(request: HttpRequest):
    
    blogs = Blog.objects.all()

    return render(request, "main/home_page.html", {"blogs": blogs})

def add_page(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],
                        contant=request.POST["contant"], 
                        image = request.FILES["image"],
                        is_published=request.POST["is_published"], 
                        publish_date=date.today())
        new_blog.save()
        return redirect("main:home_page")
    return render(request, "main/add_page.html")

def read_blog(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Exception:
        return redirect("main:notfoundpafe")

    return render(request, "main/read_blog.html", {"blog": blog})

def update_blog(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    # iso_date = blog.publish_date.isoformat()

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.contant = request.POST["contant"]
        if 'image' in request.FILES :
            blog.image = request.FILES["image"]
        blog.is_published = request.POST["is_published"]
        blog.save()

        return redirect('main:read_blog', blog_id=blog.id)

    return render(request, "main/update_blog.html", {"blog": blog})

def delete_blog(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('main:home_page')


def search_blog(request:HttpRequest):
    get_quiry = request.GET.get("search", "")
    blogs = Blog.objects.filter(title__contains=get_quiry, is_published = True)

    return render(request, "main/search_page.html", {"blogs": blogs})

def notfoundpafe(request:HttpRequest):
    return render(request, "main/notfoundpafe.html")