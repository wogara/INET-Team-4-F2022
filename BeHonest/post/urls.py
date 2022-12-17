from . import views
from django.urls import path

app_name = "post"
urlpatterns = [
    path("", views.post_list, name="base"),
    path("<int:id>/", views.post_detail, name="post_detail"),
    path("news/<int:id>/", views.news_detail, name="news_detail"),
    # path("logout/", views.logout_request, name="logout"),
    path("like/<int:pk>", views.like_post, name="like_post"),
    path("profile/<str:pk>", views.profile, name="profile"),
    path("dislike/<int:pk>", views.dislike_post, name="dislike_post"),
    path("react/<int:pk>", views.react_post, name="react_post"),
    path("delete/<int:pk>", views.delete_post, name="delete_post"),
    path("delete_user/<str:pk>/", views.delete_user, name="delete_user"),
    path("search_results", views.search_results, name="search-results"),
    path("prof_results", views.prof_results, name="prof-results"),
    path("edit/<int:pk>", views.post_update, name="post_update"),
]
