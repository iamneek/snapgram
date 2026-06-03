from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from django.core.paginator import Paginator

def feed_view(request):
    page_num = request.GET.get('page', 1)
    post_paginator = Paginator(Post.objects.all().order_by('-created_at'), 10)
    page_obj = post_paginator.get_page(page_num)
    
    if request.headers.get('HX-Request'):
        return render(request, 'posts/feed_posts.html', {'page_obj' : page_obj})
    
    return render(request, 'feed.html', {'page_obj': page_obj})


@login_required
def create_post_view(request):
    pass


@login_required
def toggle_like(request, post_id):
    pass


@login_required
def create_comment_view(request, post_id):
    pass

@login_required
def delete_comment_view(request, comment_id):
    pass

