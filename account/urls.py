from django.urls import path

from account import views
app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("profile/", views.profile_view, name="profile"),

]