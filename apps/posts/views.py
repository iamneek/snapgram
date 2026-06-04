from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Like, Comment
from django.core.paginator import Paginator
from django.db import transaction, IntegrityError
from django.http import HttpResponse


@login_required
def feed_view(request):
    page_num = request.GET.get("page", 1)
    post_paginator = Paginator(Post.objects.all().order_by("-created_at"), 10)
    page_obj = post_paginator.get_page(page_num)
    liked_post_ids = set(
        Like.objects.filter(user=request.user).values_list("post_id", flat=True)
    )

    if request.headers.get("HX-Request"):
        return render(
            request,
            "posts/feed_posts.html",
            {"page_obj": page_obj, "liked_post_ids": liked_post_ids},
        )

    return render(
        request, "feed.html", {"page_obj": page_obj, "liked_post_ids": liked_post_ids}
    )


@login_required
def create_post_view(request):
    pass


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        try:
            with transaction.atomic():
                like, created = Like.objects.get_or_create(post=post, user=request.user)
                if not created:
                    like.delete()
                    user_liked = False
                else:
                    user_liked = True
        except IntegrityError:
            user_liked = Like.objects.filter(post=post, user=request.user).exists()

    if request.headers.get("HX-Request"):
        user_liked = Like.objects.filter(post=post, user=request.user).exists()
        return render(
            request, "posts/like_button.html", {"post": post, "user_liked": user_liked}
        )
    else:
        return redirect("feed")


@login_required
def create_comment_view(request, post_id):
    if request.method == "POST":
        content = request.POST.get("comment_content").strip()
        if not content:
            messages.error(request, "Please enter a valid message!!")
            return redirect("feed")

        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(post=post, author=request.user, content=content)
        return render(
            request,
            "posts/comment_list.html",
            {'comments': post.comments.select_related('author')},
        )

    return redirect("feed")


@login_required
def delete_comment_view(request, comment_id):
    if request.method == "POST":
        cmnt = get_object_or_404(Comment, id=comment_id, author=request.user)
        post = cmnt.post
        cmnt.delete()
        return HttpResponse("")
    return redirect("feed")


@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked_post_ids = set(
        Like.objects.filter(user=request.user).values_list("post_id", flat=True)
    )
    return render(request, 'posts/post_detail.html', {"post":post, "liked_post_ids": liked_post_ids,     "comments": post.comments.select_related('author')
})
