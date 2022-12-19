from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.shortcuts import redirect
from django.urls import reverse
from blogs.blog.form import SearchForm
from functools import wraps, lru_cache


def get_minimized_text(text, length=30):
    if len(text) <= length:
        return text
    return text[:length] + "..."


@lru_cache(maxsize=100, typed=True)
def pagination(request, object_list, page_limit=10):
    paginator = Paginator(object_list, page_limit)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return results


@lru_cache(maxsize=100, typed=True)
def full_text_search(request, obj):
    q = request.GET.get("query")
    if q:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            obj = (
                obj.annotate(
                    similarity=Greatest(
                        TrigramSimilarity("title", query),
                        TrigramSimilarity("body", query),
                    )
                )
                .filter(similarity__gte=0.05)
                .order_by("-similarity")
            )
    return obj, q


def redirect_if_search(func):
    @wraps(func)
    def wrapper(request, **kwargs):
        cat_slug = kwargs.get("cat_slug")
        if "query" in request.GET and cat_slug != "search":
            query = request.GET.get("query")
            return redirect(
                f'{reverse("blogs:post_cat_view", kwargs={"cat_slug": "search"})}?query={query}'
            )
        else:
            return func(request, **kwargs)

    return wrapper
