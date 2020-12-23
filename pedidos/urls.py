from django.urls import path
from pedidos.views import *

urlpatterns = [
    path('login/', login_user, name= 'login'),
    path('home/', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('teste/', teste, name='teste')
]