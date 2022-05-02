from rest_framework import generics

from core.models import Actor
from .serializers import ActorSerializer


class ActorDetailView(generics.RetrieveAPIView):
    """Actor information"""
    serializer_class = ActorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        actor_id = self.kwargs['id']
        return Actor.objects.filter(id=actor_id)
