from django.urls import path
from . import views

urlpatterns = [
   # path("", views.starting_page, name="starting-page"),
    # path("posts", views.posts, name="posts-page"),
    path("", views.staring_page.as_view(), name="starting-page"),
    path("posts",views.allPostListView.as_view(),name="posts-page"),
    path("posts/<slug:slug>", views.post_detail.as_view(), name="post-detail-page"),
    #path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
    path("read-latter", views.ReadLaterView.as_view(),name="read-later")
]
