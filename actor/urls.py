from django.urls import path
from . import views

urlpatterns = [
    path('actors1111111/', views.index, name='index1'),
    path("actor/detail/<int:pk>/", views.actor, name="detail"),
    path("search_actor/", views.SearchActor.as_view(), name='search_actor'),
    path("actors/add_actor/", views.add_actor, name='add_actor')

]