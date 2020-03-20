from django.urls import path, include
from movies import views


urlpatterns = [
    path('top/', views.TopMoviesListView.as_view(), name='all_movies'),
    path('<int:pk>/', views.MoviesDetailView.as_view(), name='detailed_movie'),
    path('<int:pk>/voting/', views.voting, name='voting'),
    path('<int:pk>/comments/', views.add_comment, name='comment'),
    path('latest/', views.NewMoviesListView.as_view(), name='latest'),
    path('actors/', include('actress.urls')),
    path('result/', views.search_movie, name='result'),
]
