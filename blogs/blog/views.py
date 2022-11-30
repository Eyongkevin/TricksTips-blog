from django.shortcuts import render, get_object_or_404

from .models import Post
from blogs.like.models import Like
from blogs.category.models import Category
from .utils import pagination, full_text_search, redirect_if_search
from .form import SearchForm

# Create your views here.


@redirect_if_search
def index_view(request, **kwargs):
    form = SearchForm()
    return render(
        request,
        "blog/index.html",
        {"form": form},
    )


@redirect_if_search
def post_list(request, **kwargs):
    """get all posts by cat."""

    form = SearchForm()
    cat_slug = kwargs.get("cat_slug")

    object_list = Post.post.published().order_by(
        "-likes__like_count", "-published_date"
    )

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
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "cat": cat,
            "related_posts": related_posts,
            "form": form,
        },
    )
