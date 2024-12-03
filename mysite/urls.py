"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def logout_view(request):
    logout(request)
    return redirect('/login')


# def sign_up_view(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in after successful sign-up
#             return redirect('/login')
#     else:
#         form = SignUpForm()

#     return render(request, 'signup.html', {'form': form})

def signup_view(request):
	# if request.user.is_authenticated:
	# 	return redirect('/login')
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password')
			# user = authenticate(username=username, password=password)
			# login(request, user)
			return redirect('/login')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = SignUpForm()

	return render(request, 'signup.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("/login")
    template_name = "signup.html"


urlpatterns = [
    path("", include("blogging.urls")),
    path("polling/", include("polling.urls")),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    # path("logout/", LogoutView.as_view(next_page='/login'), name="logout"),   # doesn't work
    path("logout/", logout_view, name="logout"),
    path('signup/', signup_view, name='sign_up'),
    # path("", include("django.contrib.auth.urls")),
    # path("accounts/", include("accounts.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
]
