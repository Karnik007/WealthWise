from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('i1.html/', views.i1, name='i1'),
    path('i1.html/add-income/', views.add_income, name='add_income'),
    path('i1.html/add-expense/', views.add_expense, name='add_expense'),
    path('G.html/', views.G, name='G'),
    path('b1.html/', views.b1, name='b1'),
    path('b1.html/add-bill/', views.add_bill, name='add_bill'),
    path('delete_bill/<int:bill_id>/', views.delete_bill, name='delete_bill'),  # Add the delete_bill URL pattern
]
