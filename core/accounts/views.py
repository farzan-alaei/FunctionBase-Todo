from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
            else:
                return render(request, 'accounts/login.html', {'form': form})
        
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    
    else:
        return redirect('/')


def logout_view(request):
    pass

def register_view(request):
    pass