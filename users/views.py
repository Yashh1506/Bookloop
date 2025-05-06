from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from books.models import books
from . models import UserProfile, Message


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
        else:
            user = User.objects.create(
                username=username,
                email=email,
                first_name = firstname,
                last_name = lastname,
                password=make_password(password)
            )
            UserProfile.objects.create(user=user)
            messages.success(request, "User is successfully registered")
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password')
    return render(request, 'login.html')


def home(request):
    featured_books = books.objects.all()[:2]
    return render(request, 'index.html',{'featured_books': featured_books })


# @login_required
# def profile(request, user_id):
#     return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def users(request, user_id):
    return render(request, 'profile.html')

@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    all_books = books.objects.filter(user=request.user)
    user = request.user
    preferences = userprofile.preferences.split(',') if userprofile.preferences else []
    return render(request, 'profile.html', {'userprofile':userprofile, 'viewed_user':user, 'preferences':preferences, 'all_books':all_books})

@login_required
def edit_profile(request):
    user = request.user
    userprofile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('profile_pic')
        bio = request.POST.get('bio')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        preferences = request.POST.getlist('preferences')
        exchange_preferences = request.POST.getlist('exchange_preferences')

        if User.objects.filter(email=email).exclude(id=user.id).exists():
            messages.error(request, "Email already exists")
        else:
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

            if profile_pic:
                userprofile.profile_pic = profile_pic
            userprofile.bio = bio
            userprofile.city = city
            userprofile.state = state
            userprofile.country = country
            userprofile.preferences = ','.join(preferences)
            userprofile.exchange_preferences = ','.join(exchange_preferences)
            userprofile.save()

            return render(request, 'profile.html')
            

    return render(request, 'edit-profile.html', {'userprofile':userprofile, 'user':user})

@login_required
def chat_view(request, username):
    user = request.user
    previous_chat_users = User.objects.filter(
        Q(sent_messages__receiver=request.user) | Q(received_messages__sender=request.user)
    ).distinct().exclude(id=request.user.id)
    other_user = get_object_or_404(User, username=username) if username else user.first()

    if request.method == "POST":
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=user, receiver=other_user, content=content)
            return redirect('chat', username=other_user.username)
        
    messages = Message.objects.filter(
        sender__in = [user, other_user],
        receiver__in = [user, other_user]
    ).order_by('timestamp') if other_user else []

    return render(request, 'chat/chat.html', {'messages':messages, 'other_user':other_user, 'users':previous_chat_users})

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    userprofile = get_object_or_404(UserProfile, user=user)
    all_books = books.objects.filter(user=user)
    preferences = userprofile.preferences.split(',') if userprofile.preferences else []
    return render(request, 'profile.html', {
        'viewed_user':user,
        'userprofile': userprofile,
        'preferences':preferences,
        'all_books':all_books,
        'username':username
    })



    


