from django.urls import path
from.views import AuthorsList, AuthorDetail, PostList, PostDetail


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('authors', AuthorsList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
]