from django.urls import path

from feed import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>', views.profile, name='profile'),
    path('', views.index, name='new-post'),
    path('', views.index, name='edit-profile'),
]
