from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostFormOne, PostFormTwo
from .models import *


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def alltext(request):
    text = Post.objects.values('text')
    return render(request, 'blog/alltext.html', {'text': text})


def form_one(request):
    if request.method == 'POST':
        form = PostFormOne(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('post_list')
    else:
        form = PostFormOne()
    return render(request, 'blog/form_one.html', {'form': form})


def form_two(request):
    form = PostFormTwo()
    return render(request, 'blog/form_two.html', {'form': form})
