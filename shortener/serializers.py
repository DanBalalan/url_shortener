from rest_framework import serializers
from . import models


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = ['id', 'user', 'url_original', 'url_part_short', 'date_created', 'usage_count']
