from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact_us, name='contact'),
    path('thanks/', views.submit_message, name='messagesent'),
    path('<int:pk>/watchlist', views.add_watch_list, name='watchlist'),
    path('watchlist/', views.watch_list_func, name='watchlist_func'),
    path('<int:pk>/delete/', views.delete_watch_list, name='delete'),
]
