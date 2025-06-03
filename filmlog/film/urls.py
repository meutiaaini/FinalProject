from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    path('film/<int:film_id>/review/', views.add_review, name='add_review'),
]
