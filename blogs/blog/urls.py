from django.urls import path
from . import views

app_name = "blogs"

urlpatterns = [
    path("", views.index_view, name="blogs_index"),
    path("tag/<slug:tag_slug>/", views.post_list, name="post_tag_view"),
]
