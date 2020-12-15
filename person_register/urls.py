from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('', views.home, name="home"),
    path('create_person/', views.createPerson, name="create_person"),
    path('update_person/<str:pk>/', views.updatePerson, name="update_person"),
    path('delete_person/<str:pk>/', views.deletePerson, name="delete_person"),
    path(r'/auth/', ObtainAuthToken.as_view()),
]