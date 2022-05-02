from rest_framework import serializers

from core.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serialize a movie"""

    class Meta:
        model = Movie
        fields = '__all__'
