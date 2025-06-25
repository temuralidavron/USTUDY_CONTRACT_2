from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect


def register(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')

    else:
        form=CustomUserCreationForm()

    return render(request, 'account/register.html', {'form':form})




def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('contract:home')
            else:
                form.add_error(None, "Foydalanuvchi nomi yoki parol noto‘g‘ri!")
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('contract:home')