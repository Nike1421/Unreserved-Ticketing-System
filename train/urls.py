from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('schedule/', views.schedule, name='schedule'),
    path('quickroutes/', views.quickroutes, name='quickroutes'),
    path('bookticket/', views.bookticket, name='bookticket'),
    path('payment/', views.payment, name='payment'),
    path('fare/', views.fare, name='fare'),
    path('otp/', views.otp, name='otp'),
    path('blank/', views.blank, name='blank'),
    path('bookedticket/', views.bookedticket, name='ticket')
]