from django.urls import path
from .views import SongList, SongDetail


urlpatterns = [
    path('<int:pk>/', SongDetail.as_view()),
    path('', SongList.as_view()),
]