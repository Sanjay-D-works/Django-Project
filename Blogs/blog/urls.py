from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("", views.index, name="Index"),
    path("post/<str:post_id>", views.details, name="detail"),
    path("new_something_url",views.new_url_view, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url")


]