from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from core.models import Actor


def detail_url(actor_id: int):
    return reverse('actor:actor_stats', args=[actor_id])


class ActorAPITests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_actor_page(self):
        """Test that actor page returns 200"""
        actor = Actor.objects.create(
            first_name='first_name',
            last_name='last_name',
            gender='M'
        )
        url = detail_url(actor.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
