from django.shortcuts import render, get_object_or_404

from .models import Post
from blogs.like.models import Like
from blogs.category.models import Category
from .utils import pagination, full_text_search, redirect_if_search
from .form import SearchForm

# Create your views here.


@redirect_if_search
def index_view(request, **kwargs):
    # get all categories
    all_cats = Category.objects.all()
    # get at least 10 hot posts(with highest likes)
    hot_posts = Like.like.most_liked_posts()
    form = SearchForm()
    return render(
        request,
        "blog/index.html",
        {"cats": all_cats, "hot_posts": hot_posts, "form": form},
    )


@redirect_if_search
def post_list(request, **kwargs):
    """get all posts by cat."""

    all_cats = Category.objects.all()
    form = SearchForm()
    cat_slug = kwargs.get("cat_slug")

    object_list = Post.post.published().order_by(
        "-likes__like_count", "-published_date"
    )
    hot_posts = Like.like.most_liked_posts()

    cat = None
    if cat_slug and cat_slug != "search":
        cat = get_object_or_404(Category, slug=cat_slug)
        object_list = object_list.filter(category__in=[cat])
    if cat_slug == "search" or "query" in request.GET:
        object_list, q = full_text_search(request, object_list)
        cat = {"slug": f"{cat_slug if cat_slug else 'search'}={q}"}

    posts = pagination(request, object_list)

    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "cat": cat,
            "cats": all_cats,
            "hot_posts": hot_posts,
            "form": form,
        },
    )


@redirect_if_search
def post_detail(request, **kwargs):
    cat_slug = kwargs.get("cat_slug")
    year = kwargs.get("year")
    month = kwargs.get("month")
    day = kwargs.get("day")
    post = kwargs.get("post")
    all_cats = Category.objects.all()
    form = SearchForm()
    post = get_object_or_404(
        Post,
        slug=post,
        published_date__year=year,
        published_date__month=month,
        published_date__day=day,
    )
    cat = Category.objects.filter(slug=cat_slug).first()
    tag_slugs = [tag.slug for tag in post.tags.all()]
    related_posts = (
        Post.post.published()
        .filter(
            tags__slug__in=tag_slugs,
        )
        .exclude(id=post.id)
        .order_by("likes__like_count")[:5]
    )
    hot_posts = Like.like.most_liked_posts()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "cat": cat,
            "cats": all_cats,
            "related_posts": related_posts,
            "hot_posts": hot_posts,
            "form": form,
        },
    )
