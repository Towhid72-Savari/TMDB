from django.urls import path
from actress import views

urlpatterns = [
    path('', views.ActorsListView.as_view(), name='actors'),
    path('<int:pk>/', views.DetailedActor.as_view(), name='actor_detail'),
]
