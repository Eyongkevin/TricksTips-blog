from django.shortcuts import render
from taggit.models import Tag

# Create your views here.


def index_view(request):
    # get all unique tags
    all_tags = [tag.name for tag in Tag.objects.all()]

    # get at least 10 hot posts(with highest likes)
    hot_posts = None

    return render(request, "blog/index.html", {"tags": all_tags, "posts": hot_posts})
