"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

from allauth.socialaccount import views as socialaccount_views
from allauth.account.views import LoginView, LogoutView, PasswordResetView


urlpatterns = [
    path('', views.login, name='login'),

    path('home/', include('home.urls')),
    path('chat/', include('chat.urls')),

    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/logout/', LogoutView.as_view(), name='account_logout'),
    path('accounts/password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', socialaccount_views.SignupView.as_view(), name='account_signup'),

    path('admin/', admin.site.urls),
]
