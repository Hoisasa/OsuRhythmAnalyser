from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == "POST":
        req = request.POST
        if req.get('password'):
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("DjangoService:MusicCollection")
        elif req.get('password1'):
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("DjangoService:MusicCollection")
    context = {'formRegstr': UserCreationForm(),
               'formLogin': AuthenticationForm()}
    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("DjangoService:MusicCollection")
