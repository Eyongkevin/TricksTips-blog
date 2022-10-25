from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from .models import Post
from blogs.like.models import Like
from .utils import search_filter, pagination

# Create your views here.


def index_view(request):
    # get all unique tags
    all_tags = Tag.objects.all()

    # get at least 10 hot posts(with highest likes)
    hot_posts = Like.like.most_liked_posts()

    return render(
        request, "blog/index.html", {"tags": all_tags, "hot_posts": hot_posts}
    )


def post_list(request, tag_slug=None):
    """get all posts by tag."""

    object_list = Post.post.published().order_by(
        "-likes__like_count", "-published_date"
    )
    object_list = search_filter(request, object_list)
    hot_posts = Like.like.most_liked_posts()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    posts = pagination(request, object_list)
    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "tag": tag, "hot_posts": hot_posts},
    )


def post_detail(request, tag, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        published_date__year=year,
        published_date__month=month,
        published_date__day=day,
    )
    tag = Tag.objects.filter(name=tag).first()
    return render(request, "blog/post_detail.html", {"post": post, "tag": tag})
