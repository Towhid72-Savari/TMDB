from django.shortcuts import render, get_object_or_404, redirect
from movies import models
from django.views.generic import ListView, DetailView


# Create your views here.
def home_page(request):
    page_title = 'Home'
    movie_slid_bar = models.Movies.objects.filter(rate__gt=7)[:3]
    movies_top_rated = models.Movies.objects.filter(rate__gte=8).order_by('-rate')[:12]
    new_movies = models.Movies.objects.filter(release_date__year__gte='2019')[:6]
    famous_actors = models.Actor.objects.filter()[:6]
    return render(request, 'movies/home.html', {'movie_slid_bar': movie_slid_bar,
                                                'movies_top_rated': movies_top_rated,
                                                'new_movies': new_movies,
                                                'famous_actors': famous_actors,
                                                'page_title': page_title})


class TopMoviesListView(ListView):
    template_name = 'movies/all_movies.html'
    model = models.Movies
    paginate_by = 10

    def get_queryset(self):
        return models.Movies.objects.filter(rate__gte=8).order_by('-rate')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Top Movies'
        return context


class NewMoviesListView(ListView):
    template_name = 'movies/new_movies.html'
    model = models.Movies
    paginate_by = 10

    def get_queryset(self):
        return models.Movies.objects.filter(release_date__year__gte=2019).order_by('-rate')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'New Movies'
        return context


class MoviesDetailView(DetailView):
    model = models.Movies
    template_name = 'movies/detailed_movie.html'

    def get_context_data(self, **kwargs):
        related = self.object.genre.split(',')[0]
        context = super().get_context_data(**kwargs)
        context['related'] = models.Movies.objects.filter(genre__contains=related).filter(rate__gte=8).exclude(
            title=self.object.title)[:6]
        context['listed'] = models.Movies.objects.filter(movie_on_list__user_who_add_to_list_id=self.request.user.pk)
        context['rated'] = models.Movies.objects.filter(rated__user_rater_id=self.request.user.pk)
        context['page_title'] = self.object.title
        return context


def voting(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(models.Movies, pk=pk)
        rater = models.UserRater.objects.create(movie_rated=movie,
                                                user_rater=request.user,
                                                user_rate=int(request.POST['vote_value']))
        rater.save()
        movie.rate_counter += 1
        movie.rate = (movie.rate + int(request.POST['vote_value'])) / movie.rate_counter
        movie.save()
        return redirect('/movies/' + str(pk))
    else:
        return redirect('/movies/' + str(pk))


def add_comment(request, pk):
    if request.method == 'POST':
        movie = get_object_or_404(models.Movies, pk=pk)
        user = request.user
        comment = models.Comment.objects.create(movie=movie, author=user,
                                                cm_text=request.POST['cm-text'])
        comment.save()
        return redirect('/movies/' + str(pk))
    else:
        return redirect('/movies/' + str(pk))


def search_movie(request):
    if request.method == 'POST':
        search_for = request.POST['search-for']
        search_results = models.Movies.objects.filter(title__icontains=search_for)
        page_title = 'Search Results for: ' + request.POST['search-for']
        return render(request, 'movies/search_result.html', {'search_results': search_results,
                                                             'search_for': search_for,
                                                             'page_title': page_title})
