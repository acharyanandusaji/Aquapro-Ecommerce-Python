from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.login, name="login"),

    # path('logout/',),

]
