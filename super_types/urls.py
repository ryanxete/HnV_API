from django.urls import path
from . import views

urlpatterns = [
    path('', views.types),
    path('<int:pk>/', views.types_detail)
]