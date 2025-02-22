from django.urls import path  
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('signup.html/',views.signup, name='signup'),
    path('i1.html/',views.i1, name='i1'),
    path('logout/',views.logout, name='logout'),
    path('Gs.html/',views.i2, name='i2'),
    path('B.html/',views.i3, name='i3'),
    path('home.html/',views.i4, name='i4'),
]
