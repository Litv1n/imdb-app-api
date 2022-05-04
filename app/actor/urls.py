from django.urls import path

from .views import ActorDetailView


app_name = 'actor'


urlpatterns = [
    path('actor_stats/<int:id>/', ActorDetailView.as_view(), name='actor_stats'),
]
