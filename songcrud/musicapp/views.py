from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Artiste, Song, Lyrics
# Create your views here.


class MusicBaseView(View):
    model = Artiste, Song, Lyrics
    fields = '__all__'
    success_url = reverse_lazy('musicapp:all')


class MusicListView(MusicBaseView, ListView):
    pass


class MusicCreateView(MusicBaseView, CreateView):
    pass


class MusicUpdateView(MusicBaseView, UpdateView):
    pass


class MusicDetailView(MusicBaseView, DetailView):
    pass


class MusicDeleteView(MusicBaseView, DeleteView):
    pass
