from django.urls import path
from Website import views

# TEMPLATE TAGGING
app_name='Website'

urlpatterns = [
    # path('home', views.home, name='home'),
    path('help', views.help, name='help'),
    # path('user', views.user, name='user'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout')
    # path('signup', views.signup, name='signup')
]