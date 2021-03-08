from django.urls import path

from feed import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'user/<str:username>', views.profile, name='profile'),
    path(r'new-post/', views.new_post, name='new-post'),
    path(r'edit-profile/', views.edit_profile, name='edit-profile'),
    path(r'post/<int:id>', views.post, name='post'),
]
