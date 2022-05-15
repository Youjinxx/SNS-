import re
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def main(request):
    return render(request, 'main/mainpage.html')

def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html',{'posts':posts})

def showsub(request):
    return render(request, 'main/subpage.html')

def detail(request,id):
    post=get_object_or_404(Post, pk=id)
    return render(request,'main/detail.html',{'post':post})

def new(request):
    return render(request,'main/new.html')

def create(request):
    new_post = Post()
    new_post.title=request.POST['title']
    new_post.writer=request.POST['writer']
    new_post.pub_date=timezone.now()
    new_post.body=request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    upate_post = Post.objects.get(id=id)
    upate_post.title = request.POST['title']
    upate_post.writer = request.POST['writer']
    upate_post.pub_date = timezone.now()
    upate_post.body = request.POST['body']
    upate_post.save()
    return redirect('main:detail', upate_post.id)

def delete(request,id):
    delete_post=Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:posts')