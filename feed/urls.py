from django.urls import path

from feed import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'user/<str:username>', views.profile, name='profile'),
    path('', views.index, name='new-post'),
    path(r'edit-profile/', views.edit_profile, name='edit-profile'),
]
