from django.shortcuts import render
from django.views.generic import ListView, DetailView
from actress import models
from movies.models import Movies


# Create your views here.
class ActorsListView(ListView):
    template_name = 'actress/all_actors.html'
    model = models.Actor
    paginate_by = 10

    def get_queryset(self):
        return models.Actor.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Actors'
        return context


class DetailedActor(DetailView):
    template_name = 'actress/detailed_actor.html'
    model = models.Actor

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.name
        return context
