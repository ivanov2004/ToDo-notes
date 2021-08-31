from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="note"),
	path('update_note/<str:pk>/', views.updateNote, name="update_note"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),
]