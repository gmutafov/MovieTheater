from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path("", views.ProfileDetailView.as_view(), name="profile"), <------ future function
    path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),

]