from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index_view, name="blogs_index"),
    path("cat/<slug:cat_slug>/", views.post_list, name="post_cat_view"),
    path(
        "<slug:cat_slug>/<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
]
