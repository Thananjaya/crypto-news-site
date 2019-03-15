from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('costs/', views.costs, name="costs")
]
