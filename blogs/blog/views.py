from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from .models import Post
from blogs.like.models import Like
from blogs.category.models import Category
from .utils import search_filter, pagination

# Create your views here.


def index_view(request):
    # get all categories
    all_cats = Category.objects.all()

    # get at least 10 hot posts(with highest likes)
    hot_posts = Like.like.most_liked_posts()

    return render(
        request, "blog/index.html", {"cats": all_cats, "hot_posts": hot_posts}
    )


def post_list(request, cat_slug=None):
    """get all posts by cat."""

    all_cats = Category.objects.all()

    object_list = Post.post.published().order_by(
        "-likes__like_count", "-published_date"
    )
    object_list = search_filter(request, object_list)
    hot_posts = Like.like.most_liked_posts()

    cat = None
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        object_list = object_list.filter(category__in=[cat])

    posts = pagination(request, object_list)

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "cat": cat, "cats": all_cats, "hot_posts": hot_posts},
    )


def post_detail(request, cat_slug, year, month, day, post):
    all_cats = Category.objects.all()
    post = get_object_or_404(
        Post,
        slug=post,
        published_date__year=year,
        published_date__month=month,
        published_date__day=day,
    )
    cat = Category.objects.filter(slug=cat_slug).first()
    return render(
        request, "blog/post_detail.html", {"post": post, "cat": cat, "cats": all_cats}
    )
