from django.urls import path

from .views import ActorDetailView


urlpatterns = [
    path('actor_stats/<int:id>/', ActorDetailView.as_view()),
]
