from django.urls import path
from . import views

app_name = 'musicapp'

urlpatterns = [
    path('' , views.MusicListView.as_view(), name = 'all') ,
    path('music/<int:pk>/detail' , views.MusicDetailView.as_view(), name = 'music_detail') ,
    path('music/create/' , views.MusicCreateView.as_view(), name = 'music_create') ,
    path('music/<int:pk>/update/' , views.MusicUpdateView.as_view(), name = 'music_update') ,
    path('music/<int:pk>/delete/' , views.MusicDeleteView.as_view(), name = 'music_delete') ,
]