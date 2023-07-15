from django.contrib import admin
from django.urls import path
from AppChat.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chatbot, name="chatbot"),
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
]
