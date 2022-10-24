from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_minimized_text(text, length=30):
    if len(text) <= length:
        return text
    return text[:length] + "..."


def pagination(request, object_list, page_limit=2):
    paginator = Paginator(object_list, page_limit)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return results


def search_filter(request, obj):
    q = request.GET.get("q")
    if q:
        return obj.filter(title__icontains=q)
    return obj
