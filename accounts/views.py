from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Movies
from accounts.models import UserWatchList
from django.contrib.auth.views import login_required


# Create your views here.
def signup(request):
    error = {}
    page_title = 'Sign Up'
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(email=request.POST['email'])
                error["email"] = "Already taken"
                return render(request, 'accounts/signup.html', {'error': error, 'page_title': page_title})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'],
                                                email=request.POST['email'])
                user.first_name = request.POST['firstname']
                user.save()
                auth.login(request, user)
                return redirect('home')
        else:
            error['password'] = 'Passwords does not match'
            return render(request, 'accounts/signup.html', {'error': error, 'page_title': page_title})
    else:
        return render(request, 'accounts/signup.html', {'page_title': page_title})


def login(request):
    error = {}
    page_title = 'Login'
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            error["auth_user"] = "Username or Password does not correct"
            return render(request, 'accounts/login.html', {'error': error, 'page_title': page_title})
    else:
        return render(request, 'accounts/login.html', {'page_title': page_title})


def contact_us(request):
    return render(request, 'accounts/contact.html', {'page_title': 'Contact us'})


def submit_message(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = 'towhid.lyft@gmail.com'
        headers = {'Reply-To': request.user.email}
        if subject and message and from_email:
            try:
                msg = EmailMessage(subject, message, from_email, ['towhid.savari@gmail.com'], headers=headers)
                msg.send()

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'accounts/thanks_page.html', {'page_title': 'Thanks'})
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')


def add_watch_list(request, pk):
    if request.method == 'POST':
        movie_item = get_object_or_404(Movies, pk=pk)
        print(movie_item)
        user_item = User(pk=request.user.pk)
        print(user_item)
        user_list = UserWatchList()
        user_list.movie_added_to_list = movie_item
        user_list.user_who_add_to_list = user_item
        user_list.save()
        return redirect('/movies/' + str(pk))


@login_required
def watch_list_func(request):
    user_watch_list = Movies.objects.filter(movie_on_list__user_who_add_to_list_id=request.user.pk)
    return render(request, 'accounts/watch_list.html', {'user_watch_list': user_watch_list,
                                                        'page_title': request.user.first_name + '\'s Watchlist'})


def delete_watch_list(request, pk):
    UserWatchList.objects.filter(movie_added_to_list_id=pk,
                                 user_who_add_to_list_id=request.user.pk).delete()
    return redirect('accounts:watchlist_func')
