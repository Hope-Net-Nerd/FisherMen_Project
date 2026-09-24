

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Post
import re
# Create your views here.



def ensure_http_urls(text):
    """
    Finds bare domain names like 'youtube.com' or 'youtube.com/watch?v=...'
    and adds 'https://' so Django's urlize can process them.
    """
    pattern = r'(?<!http://)(?<!https://)\b([a-zA-R0-9.-]+\.(?:com|org|net|co|io|tv|me|za|info)[^\s]*)\b'
    return re.sub(pattern, r'https://\1', text)

def home(request):
   return render(request, "core/home.html",)


def about(request):
   return render(request, "core/about.html",)

def books(request):
   return render(request, "core/books.html",)

def blogs(request):
   posts = Post.objects.all()
   
   return render(request,"core/media.html",{"posts":posts})





@login_required(login_url="/secret-author-doorway-99/")
def create_post(request):
    
    if request.method == 'POST':
        post_title = request.POST.get("title")
        post_content = request.POST.get("content")
        formatted_content = ensure_http_urls(post_content)
            
        if post_title and post_content:
           Post.objects.create(
            title=post_title,
            content=formatted_content,
            author=request.user
            )
           return redirect("home")
    return render(request, "core/blog.html")


@login_required
def edit_media(request, pk):
   media = get_object_or_404(Post, pk=pk)

   if media.author != request.user:
      return HttpResponseForbidden("You are not allowed to edit this blog!")
   if request.method =="POST":
      media.title = request.POST.get("title")
      media.content = ensure_http_urls(request.POST.get("content"))
      
      media.save()

      return redirect("blogs")
   return render(request, "core/edit_media.html", {"media":media})



@login_required
def delete_media(request, pk):
   media = get_object_or_404(Post, pk=pk)
   if media.author != request.user:
      return HttpResponseForbidden("You are not allowed to delete this blog!")
   if request.method == "POST":
      media.delete()
      return redirect("blogs")
   return render(request, "core/delete_confirm.html",{"media":media})


#KatlegoMasemola -- Pass: sorloth
#LesegoHope -- pass: Rugby

